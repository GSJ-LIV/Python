def traverse():
    cur = nxt[0]
    while cur != -1:
        print(dat[cur], end=' ')
        cur = nxt[cur]
    print()

