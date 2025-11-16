# recognize_patterns.py

def is_a_star(s):
    return all(ch == 'a' for ch in s)

def is_a_star_b_plus(s):
    i = 0
    n = len(s)
    while i < n and s[i] == 'a':
        i += 1
    # need at least one b
    if i >= n or s[i] != 'b':
        return False
    while i < n and s[i] == 'b':
        i += 1
    return i == n

def is_abb(s):
    return s == "abb"

s = input("Enter string: ").strip()
print("a*:", "YES" if is_a_star(s) else "NO")
print("a*b+:", "YES" if is_a_star_b_plus(s) else "NO")
print("abb:", "YES" if is_abb(s) else "NO")
