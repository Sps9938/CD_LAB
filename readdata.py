filename = input("Enter file name: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    print("Lines:", num_lines)
    print("Words:", num_words)
    print("Characters:", num_chars)

except FileNotFoundError:
    print("File not found:", filename)
