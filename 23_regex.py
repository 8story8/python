import re

string = "Hello, I am Kiske!"

x = re.findall("am", string)
print(x)

x = re.search(r"\s", string)
print(x.start())

x = re.split(r"\s", string, 3)
print(x)

x = re.sub(r"\s", "777", string)
print(x)