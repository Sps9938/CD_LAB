ch = input("Enter a single letter: ").strip()
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input. Please enter exactly one alphabet letter.")
else:
    if ch.lower() in "aeiou":
        print(f"'{ch}' is a vowel.")
    else:
        print(f"'{ch}' is NOT a vowel.")
