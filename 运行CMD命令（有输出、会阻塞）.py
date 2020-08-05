import os

# Reference: https://www.jianshu.com/p/f95c02a66706


output = os.popen('待执行的CMD命令').read()

print(output)