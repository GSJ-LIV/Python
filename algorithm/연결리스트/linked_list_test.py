MX = 1000005
dat = [0] * MX
pre = [-1] * MX
nxt = [-1] * MX
unused = 1

def insert(addr, num):
    global unused
    dat[unused] = num            # 1. 새 원소의 데이터 저장
    pre[unused] = addr           # 2. 새 원소의 pre = 삽입할 위치   
    nxt[unused] = nxt[addr]      # 3. 새 원소의 nxt = 삽입 위치의 nxt
    if nxt[addr] != -1:          # 4. 삽입 위치 다음 노드가 존재하면
        pre[nxt[addr]] = unused  #    그 노드의 pre를 새 원소로 변경
    nxt[addr] = unused           # 5. 삽입 위치의 nxt를 새 원소로 변경 
    unused += 1                  # 6. unused 1 증가 

def erase(addr):
    nxt[pre[addr]] = nxt[addr]      # 1. 이전 노드의 nxt를 삭제할 노드의 nxt로 변경
    if nxt[addr] != -1:             # 2. 다음 노드가 존재하면
        pre[nxt[addr]] = pre[addr]  #    다음 노드의 pre를 삭제할 노드의 pre로 변경 

def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end=' ')
        cur = nxt[cur]
    print()

def insert_test():
    print("***** insert_test *****")
    insert(0, 10); traverse()
    insert(0, 30); traverse()
    insert(2, 40); traverse()
    insert(1, 20); traverse()
    insert(4, 70); traverse()

def erase_test():
    print("***** erase_test *****")
    erase(1); traverse()
    erase(2); traverse()
    erase(4); traverse()
    erase(5); traverse()

insert_test()
erase_test()