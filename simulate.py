import sys
import re
import os

if len(sys.argv) != 2:
    print("Usage: python operator_validator.py input.c")
    sys.exit(1)

infile = sys.argv[1]
if not os.path.exists(infile):
    print("Input file not found:", infile)
    sys.exit(1)

with open(infile, 'r', encoding='utf-8') as f:
    code = f.read()

# Do not treat comment contents or string/char literals as code for operator extraction
def remove_strings_and_comments(s):
    # remove strings and char literals (replace with spaces of same length)
    res = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == '"':
            res.append(' ')
            i += 1
            while i < n:
                if s[i] == '\\' and i + 1 < n:
                    res.append(' ')
                    res.append(' ')
                    i += 2
                    continue
                res.append(' ')
                if s[i] == '"':
                    i += 1
                    break
                i += 1
            continue
        if ch == '\'':
            res.append(' ')
            i += 1
            while i < n:
                if s[i] == '\\' and i + 1 < n:
                    res.append(' ')
                    res.append(' ')
                    i += 2
                    continue
                res.append(' ')
                if s[i] == '\'':
                    i += 1
                    break
                i += 1
            continue
        # comments
        if ch == '/' and i + 1 < n and s[i+1] == '/':
            res.append(' ')
            i += 2
            while i < n and s[i] != '\n':
                res.append(' ')
                i += 1
            continue
        if ch == '/' and i + 1 < n and s[i+1] == '*':
            res.append(' ')
            i += 2
            while i + 1 < n:
                if s[i] == '*' and s[i+1] == '/':
                    res.append(' ')
                    res.append(' ')
                    i += 2
                    break
                res.append(' ')
                i += 1
            continue
        res.append(ch)
        i += 1
    return ''.join(res)

clean = remove_strings_and_comments(code)

# Candidate operators – check multi-char first
multi_ops = [
    ">>=", "<<=", "++", "--", "->", "==", "!=", "<=", ">=", "&&", "||",
    "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<", ">>", "?:"
]
single_ops = [
    "+", "-", "*", "/", "%", "<", ">", "=", "&", "|", "^", "~", "!", "?", ":", ".", "->"
]
# Valid C operators set (representative)
VALID_OPERATORS = set([
    # arithmetic
    "+","-","*","/","%","++","--",
    # bitwise
    "&","|","^","~","<<",">>","<<=",">>=",
    # assignment
    "=","+=","-=","*=","/=","%=","&=","|=","^=",
    # relational
    "==","!=",">","<",">=","<=",
    # logical
    "&&","||","!",
    # conditional
    "?",
    ":",
    # other
    "->",".", "sizeof"
])

# Build regex to find operators (multi-char first)
# Escape special regex chars
op_candidates = sorted(multi_ops, key=lambda x: -len(x)) + single_ops
escaped = [re.escape(op) for op in op_candidates]
pattern = re.compile('|'.join(escaped))

found = pattern.findall(clean)

# Write operators_found.txt
with open('operators_found.txt', 'w', encoding='utf-8') as f:
    for op in found:
        f.write(op + '\n')

# Validate
invalid = []
valid = []
for op in found:
    if op in VALID_OPERATORS:
        valid.append(op)
    else:
        invalid.append(op)

# Print summary
print(f"Total operator-like tokens found: {len(found)}")
print(f"Valid operators: {len(valid)}")
print(f"Invalid/unrecognized operator-like tokens: {len(invalid)}")

if invalid:
    print("\nInvalid tokens (one per line):")
    for it in sorted(set(invalid)):
        print(it)
    with open('invalid_operators.txt', 'w', encoding='utf-8') as f:
        for it in invalid:
            f.write(it + '\n')
    print("\nWrote invalid tokens to invalid_operators.txt")

print("\nWrote all found operator tokens to operators_found.txt")
