# 构建模块  python3 setup.py build
# 生成发布压缩包  python3 setup.py sdist
# 安装模块  tar -zxvf mine_message-1.0.0.tar.gz ;cd mine_message-1.0.0  ;sudo python3 setup.py install
# 卸载模块 cd /usr/local/lib/python3.8/dist-packages/  ;  sudo rm -rf mine_message
from distutils.core import setup

setup(name="mine_message",
      version="1.0.0",
      description="发送、接受消息模块",
      long_description="发送、接受消息模块",
      author="phoenix",
      author_email="sm516116978@outlook.com",
      url="http://www.phoenix-jd.com",
      py_modules=[
          "mine_10_message.send_message",
          "mine_10_message.receive_message"
      ]
      )
