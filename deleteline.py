filename = input("Enter file name: ")
line_no = int(input("Enter line number to delete: "))

with open(filename, "r") as f:
    lines = f.readlines()

if 1 <= line_no <= len(lines):
    removed = lines.pop(line_no - 1)
    with open(filename, "w") as f:
        f.writelines(lines)
    print("Removed:", removed.strip())
else:
    print("Invalid line number")
