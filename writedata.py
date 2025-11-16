output_file = input("Enter output file name: ")

n = int(input("Enter number of students: "))

with open(output_file, "w") as f:
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = input(f"Enter marks of student {i+1}: ")
        f.write(name + " " + marks + "\n")

print("Data saved to", output_file)
