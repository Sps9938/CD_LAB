import sys

def read_input(path=None):
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return sys.stdin.read()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) == 2 else None
    text = read_input(path)
    lines = text.count('\n') + (0 if text.endswith('\n') or text=='' else 1) if text else 0
    tabs = text.count('\t')
    spaces = text.count(' ')
    # Also report total characters for convenience
    chars = len(text)
    print(f"Lines: {lines}")
    print(f"Tabs: {tabs}")
    print(f"Spaces: {spaces}")
    print(f"Total characters: {chars}")
