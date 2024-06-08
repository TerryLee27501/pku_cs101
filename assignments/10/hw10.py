def q1():
    os = input()  # original string
    s = []
    cw = ''  # current word
    for _, l in enumerate(os):
        if l == '(':
            if cw:
                s.append(cw)
                cw = ''
            s.append(l)
        elif l == ')':
            s.append(cw)
            w = ''
            while s[-1] != '(':
                w += s.pop()[::-1]
            s.pop()
            cw = w
        else:
            cw += l
    if cw:
        s.append(cw)
    print(''.join(s))


# q1()


class BTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


def q2():

    def bt(preo, ino):
        if not preo:
            return None
        root = preo[0]
        ri = ino.index(root)
        lino = ino[:ri]
        rino = ino[ri+1:]
        ll = len(lino)  # left length
        lpreo = preo[1:1+ll]
        rpreo = preo[1+ll:]
        t = BTree(root)
        t.left = bt(lpreo, lino)
        t.right = bt(rpreo, rino)
        return t

    def posto(t):
        re = ''
        if t.left:
            re += posto(t.left)
        if t.right:
            re += posto(t.right)
        re += t.node
        return re

    while True:
        try:
            preo, ino = input().split()
            print(posto(bt(preo, ino)))
        except EOFError:
            return


# q2()


from collections import deque


def q3():
    while True:
        q = deque([1])
        n = int(input())
        if n == 0:
            return
        while True:
            c = q.popleft()
            if c % n == 0:
                print(c)
                break
            else:
                q.append(c * 10)
                q.append(c * 10 + 1)


# q3()


def q4():
    m, n, t = map(int, input().split())
    graph = []
    for x in range(m):
        rs = input()  # raw string
        graph.append(rs)
        for y, l in enumerate(rs):
            if l == '@':
                s = [x, y]
            if l == '+':
                d = [x, y]

    v = [[-1] * n for _ in range(m)]
    q = deque([[s, 0, t]])
    while q:
        cp, time, hits = q.popleft()
        if v[cp[0]][cp[1]] < hits:
            v[cp[0]][cp[1]] = hits
        else:
            continue
        if cp == d:
            print(time)
            return

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ori_nps = [[cp[0]+ix, cp[1]+iy] for ix, iy in dirs]
        nps = []
        for npx, npy in ori_nps:
            if npx >= m or npx < 0 or npy >= n or npy < 0 or [npx, npy] in v:
                continue
            nps.append([npx, npy])
        for np in nps:
            if graph[np[0]][np[1]] == '#':
                if hits > 0:
                    q.append([np, time+1, hits-1])
            else:
                    q.append([np, time+1, hits])

    print(-1)
    return


# q4()


def q5():
    m, n, p = map(int, input().split())
    g = []
    for _ in range(m):
        chars = input().split()
        newcs = []
        for char in chars:
            if char == '#':
                newcs.append(char)
            elif char.isdigit():
                newcs.append(int(char))
            else:
                newcs.append(float(char))
        g.append(newcs)
    for _ in range(p):
        sx, sy, ex, ey = tuple(map(int, input().split()))
        if g[sx][sy] == '#' or g[ex][ey] == '#':
            print('NO')
            continue
        q = deque([[[sx, sy], 0]])
        s = [[1000000000]*n for i in range(m)]
        while q:
            fe = q.popleft()  # first element
            cx, cy = fe[0]
            ss = fe[1]  # strength spent
            if s[cx][cy] <= ss:
                continue
            s[cx][cy] = ss
            if (cx, cy) == (ex, ey):
                continue
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in dirs:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != '#':
                    sn = abs(g[nx][ny] - g[cx][cy])  # strength now
                    q.append([[nx, ny], ss+sn])
        es = s[ex][ey]
        if es == 1000000000:
            print('NO')
        else:
            print(es)
    return


q5()