import os
import re

# Reference: https://www.jianshu.com/p/f95c02a66706
# Need test in different conditions.

cmd = 'py -3 -V'
output = os.popen(cmd).read()
print(output)
print(len(output))
print(output.startswith('Python') and len(output) == 13)
