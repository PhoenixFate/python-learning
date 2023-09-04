# 导入整个包 package
import mine_10_message
from mine_10_message import send_message

mine_10_message.send_message.send("你好")
print(mine_10_message.receive_message.receive())
send_message.send("重新发送消息")
