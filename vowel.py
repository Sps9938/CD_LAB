# vowel_checker.py
# Usage (interactive): python vowel_checker.py
# It asks for a single character input and reports if it's a vowel.

ch = input("Enter a single letter: ").strip()
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input. Please enter exactly one alphabet letter.")
else:
    if ch.lower() in "aeiou":
        print(f"'{ch}' is a vowel.")
    else:
        print(f"'{ch}' is NOT a vowel.")
