import sys

def read_input(path=None):
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        # read from stdin
        return sys.stdin.read()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) == 2 else None
    text = read_input(path)
    capitals = [ch for ch in text if 'A' <= ch <= 'Z']
    if capitals:
        print("Capital letters found (one per line):")
        for c in capitals:
            print(c)
        print(f"Total capitals: {len(capitals)}")
    else:
        print("No capital letters found.")
