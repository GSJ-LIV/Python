import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(target_str):
    stack = []

    for ch in target_str:
        if ch in ["(", "["]:
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
    return not stack
    

def main():
    while True:
        s = sys_input()
        if s == ".":
            break

        answer = solve(s)
        print("yes" if answer else "no")

if __name__ == "__main__":
    main()