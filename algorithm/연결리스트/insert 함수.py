def insert(addr, num):
    global unused
    dat[unused] = num            # 1. 새 원소의 데이터 저장
    pre[unused] = addr           # 2. 새 원소의 pre = 삽입할 위치   
    nxt[unused] = nxt[addr]      # 3. 새 원소의 nxt = 삽입 위치의 nxt
    if nxt[addr] != -1:          # 4. 삽입 위치 다음 노드가 존재하면
        pre[nxt[addr]] = unused  #    그 노드의 pre를 새 원소로 변경
    nxt[addr] = unused           # 5. 삽입 위치의 nxt를 새 원소로 변경 
    unused += 1                  # 6. unused 1 증가 