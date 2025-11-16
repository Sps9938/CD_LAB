import sys
import re

if len(sys.argv) != 3:
    print("Usage: python normalize_whitespace.py input.txt output.txt")
    sys.exit(1)

inp = sys.argv[1]
out = sys.argv[2]

with open(inp, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any sequence of whitespace (\s includes space, tab, newline, etc.) with single space
normalized = re.sub(r'\s+', ' ', text).strip()

with open(out, 'w', encoding='utf-8') as f:
    f.write(normalized)

print(f"Normalized output written to {out}")
