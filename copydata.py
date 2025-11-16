src = input("Enter source file: ")
dst = input("Enter destination file: ")

with open(src, "r") as f1:
    content = f1.read()

with open(dst, "w") as f2:
    f2.write(content)

print("Copied successfully!")
