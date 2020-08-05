import os

# TODO: what if there are python 2 and python 3 in computer?

output = os.popen('where pythonw').read()

print(output)