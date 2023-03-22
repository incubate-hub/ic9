import ast
import sys

def check_syntax(filename):
    with open(filename, 'r') as file:
        source = file.read()
        try:
            ast.parse(source)
        except SyntaxError as e:
            print(f"Syntax error in {filename}: line {e.lineno}, column {e.offset}: {e.text.strip()}")
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python syntax_checker.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if check_syntax(filename):
        print(f"{filename} has valid syntax.")
