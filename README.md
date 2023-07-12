# Kook_MC_Bot
用于连接Kook与Minecraft服务端的Bot  
一个简单的实现例子
---
### 前置python包
- json
- khl.py
  - 用于连接kook机器人的一个python库 <https://github.com/TWT233/khl.py>
- random
  - 仅用于实现khl里的一个例子
- mcrcon
  - 用于连接Minecraft服务端控制台 <https://pypi.org/project/mcrcon/>

### config配置细则
- token : kook机器人的token密钥，注意：机器人连接方式为Websocket。
- command_channel_ID : 用于使用rcon对控制台发令的kook频道ID。
- chat_channel_ID : 用于日常聊天的kook频道ID。
- user_ID : 管理员的ID，能随处使用/cmd指令对服务端控制台下令。
- host : Minecraft服务端rcon启用的IP
- port : Minecraft服务端rcon开放的端口号
- password :  Minecraft服务端rcon连接的密码

### 使用方法
1. 在服务端`server.properties`文件中启用rcon，具体为填写其中的`rcon.port`参数与`rcon.password`参数以及`enable-rcon`参数。
2. 在kook开发者平台注册账号，并在"应用"介面下选择"新建应用"，创建一个连接方式为Websocket的机器人，并在"机器人">"邀请链接"选项中按照方法将机器人邀请至自己的Kook服务器。
3. 在Bot脚本的目录下按shift打开Powershell窗口，输入`python main.py`，即可启动机器人。

### 注意事项
1. 请注意kook服务器内频道的权限设置，rcon连接的为控制台，权限级别很高，失误的权限操作会造成较大损失。
2. 目前用/cmd指令向服务端后端发送say指令，虽然能成功执行，但是脚本窗口会弹出报错“Content不能为空”，待解决。

---
如果需要让Minecraft服务器与kook频道消息实时互传的话，这个项目或许能帮到你 <https://github.com/AnzhiZhang/ChatHub>
