import sys
# input = sys.stdin.readline

MX = 1000005
dat = [0] * MX
pos = 0

def push(val):
    global pos
    dat[pos] = val
    pos += 1

def pop():
    global pos
    pos -= 1

def top():
    return dat[pos - 1]

def main():
    global pos
    n = int(input())

    for _ in range(n):
        c = input().split()

        if c[0] == "push":
            push(int(c[1]))
        
        elif c[0] == "pop":
            if pos == 0:
                print(-1)
            else:
                print(top())
                pop()
        
        elif c[0] == "size":
            print(pos)
        
        elif c[0] == "empty":
            print(1 if pos == 0 else 0) # 삼항 연산자 

        else:
            if pos == 0:
                print(-1)
            else:
                print(top())


main()