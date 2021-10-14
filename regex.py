import re
mystring = "<!hola,<"
mys = re.sub('[^A-Za-z0-9]+', '', mystring)
print(mys)
