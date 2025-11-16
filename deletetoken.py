import re

filename = input("Enter C file name: ")

code = open(filename).read()

tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|==|!=|<=|>=|->|\+\+|--|[-+*/=;{}()\[\]]|\d+", code)

print("Tokens found:")
for t in tokens:
    print(t)
