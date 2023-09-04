import os

# os.system("终端命令")
os.system("ls")

# __import__('os').system('ls') 等价于上面两句话
# eval 可以使用终端命令
eval("__import__('os').system('ls')")
