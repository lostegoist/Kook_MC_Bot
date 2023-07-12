import json
from khl import Bot, Message
import random
import mcrcon

with open('config.json',encoding='utf-8') as f:
    config = json.load(f)

bot = Bot(token=config['token'])
host = config['host']
port = config['port']
password = config['password']
command_channel_id = int(config['command_channel_ID'])
chat_channel_id = int(config['chat_channel_ID'])
user_id = int(config['user_ID'])

help_d = """可用指令如下：
/bugbot 检查bot的精神
/read <msg> 复读姬
/roll <min> <max> <N> 投骰子，最小值+最大值+次数
"""

help_a = """管理员特殊指令如下:
/cmd <command> 控制台指令
"""
# help指令，输出简单的help信息
@bot.command(name="help")
async def world(msg: Message):
    channelx = int(msg.target_id.strip())
    if channelx == command_channel_id:
        await msg.reply(f'{help_d}\n{help_a}')
    else :
        await msg.reply(help_d)
# 测试bot是否在线的指令，本质为简单的回复指令
@bot.command(name="bugbot", case_sensitive=False)
async def bugbot(msg: Message):
    await msg.reply("小智障正在Bug上运行~，待命中~(≧ロ≦)")
# 掷骰子，前两项为数值区间，后一项为次数
@bot.command(name="roll")
async def roll(msg: Message, t_min: int, t_max: int, n: int = 1):
    result = [random.randint(t_min, t_max) for i in range(n)]
    await msg.reply(f'骰子点数为：{result}')
# 复读姬指令
@bot.command(regex='^/read(.+)')
async def read(msg: Message,txt: str):
    channelx = int(msg.target_id.strip())
    if channelx != chat_channel_id:
        await msg.reply(f'该频道不予复读噢~请勿打扰他人~ (`･ω･´)')
    else : 
        await msg.reply(f'{txt.strip()}')

# 命令指令，通过rcon连接Minecraft服务器控制台，属于危险指令
@bot.command(regex='^/cmd(.+)')
async def cmd(msg: Message,cmdm: str):
    channelx = int(msg.target_id.strip())
    userx = int(msg.author_id.strip())
    if channelx != command_channel_id:
        if userx != user_id:
            await msg.reply(f'非法频道不予使用cmd! ヽ(`Д´)ﾉ')
        elif userx == user_id:
            rcon = mcrcon.MCRcon(host,password,port)
            rcon.connect()
            response = rcon.command(cmdm.strip())
            await msg.reply(response)
            rcon.disconnect()
            await msg.reply(f'请谨慎在公开场合使用~(ʘᴗʘ)')
    elif channelx == command_channel_id:
        rcon = mcrcon.MCRcon(host,password,port)
        rcon.connect()
        response = rcon.command(cmdm.strip())
        await msg.reply(response)
        rcon.disconnect()
bot.run()