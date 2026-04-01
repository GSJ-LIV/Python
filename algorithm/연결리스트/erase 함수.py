def erase(addr):
    nxt[pre[addr]] = nxt[addr]      # 1. 이전 노드의 nxt를 삭제할 노드의 nxt로 변경
    if nxt[addr] != -1:             # 2. 다음 노드가 존재하면
        pre[nxt[addr]] = pre[addr]  #    다음 노드의 pre를 삭제할 노드의 pre로 변경