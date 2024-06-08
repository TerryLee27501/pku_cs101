def q1():
    n = int(input())
    t = {}
    p = [False] * n
    for i in range(n):
        t[i+1] = list(map(int, input().split()))
        for j in t[i+1]:
            if j != -1:
                p[j-1] = True
    root = p.index(False) + 1
    kq = [root]
    re = []
    while kq:
        re.append(kq[-1])
        pq = kq
        kq = []
        for p in pq:
            ks = t[p]
            for k in ks:
                if k != -1:
                    kq.append(k)
    print(' '.join(map(str, re)))
    return


def q2():
    n = int(input())
    ns = [0] + list(map(int, input().split()))
    re = {}
    s = []
    for i in range(1, 1+n):
        while s and ns[s[-1]] < ns[i]:
            ns[s.pop()] = i
        s.append(i)
    while s:
        ns[s.pop()] = 0
    print(' '.join(map(str, ns[1:])))
    return


from collections import deque


def q3():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        ins = [0] * n
        g = {}
        v = []
        for _ in range(m):
            x, y = map(int, input().split())
            ins[y-1] += 1
            if x in g.keys():
                g[x].append(y)
            else:
                g[x] = [y]

        q = deque([])
        for i, ind in enumerate(ins):
            if ind == 0:
                q.append(i+1)
        while q:
            c = q.popleft()
            v.append(c)
            if c in g.keys():
                for e in g[c]:
                    if ins[e-1] == 0:
                        continue
                    ins[e-1] -= 1
                    if ins[e-1] == 0:
                        q.append(e)
        print('No' if len(v) == n else 'Yes')
    return


def q4():
    n, m = map(int, input().split())
    ns = [int(input()) for _ in range(n)]
    cmax = 10000000000000000000000

    def par(n, m, ns):
        if m == 1:
            sumi = sum(ns)
            if sumi >= cmax:
                return []
            else:
                return [[sumi]]
        re = []
        for i in range(n-m+1):
            sumi = [sum(ns[:i+1])]
            if sumi >= cmax: continue
            subs = par(n-1-i, m-1, ns[i+1:])
            if not subs: continue
            rei = [sumi + l for l in subs]
            re.extend(rei)
        return re

    print(par(n, m, ns))
    return


import heapq


def q5():
    k, n, r = [int(input()) for _ in range(3)]
    rs = [[] for _ in range(n+1)]
    ds = [[1000000000]*(k+1) for _ in range(n+1)]
    for _ in range(r):
        s, d, l, t = list(map(int, input().split()))
        rs[s].append((d, l, t))
    h = []
    heapq.heappush(h, (0, 1, 0))
    ds[1][0] = 0
    while h:
        d, cp, tf = heapq.heappop(h)  # current point, distance, total fee
        if cp == n:
            print(d)
            return
        if ds[cp][tf] < d: continue
        for np, l, t in rs[cp]:
            if tf + t <= k and ds[np][tf+t] > d + l:
                ds[np][tf+t] = d + l
                heapq.heappush(h, (d+l, np, tf+t))
    print(-1)
    return


def q6():
    n, k = map(int, input().split())
    p = [_ for _ in range(3*n+1)]
    re = 0

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        p[find(x)] = find(y)

    for _ in range(k):
        op, x, y = map(int, input().split())
        if x > n or y > n:
            re += 1
            continue
        if op == 1:
            if find(y) != find(x+n) and find(y) != find(x+2*n):
                union(x, y)
                union(x+n, y+n)
                union(x+2*n, y+2*n)
            else:
                re += 1
        else:
            if find(y) != find(x) and find(y) != find(x+2*n):
                union(x, y+2*n)
                union(x+n, y)
                union(x+2*n, y+n)
            else:
                re += 1
    print(re)
    return


def q4():
    n, m = map(int, input().split())
    exs = [int(input()) for _ in range(n)]

    def valid(limit):
        ce = 0  # current expenses
        fajo = 1
        for ex in exs:
            if ce + ex <= limit:
                ce += ex
            else:
                fajo += 1
                if fajo > m: return False
                ce = ex
        return True

    left = max(exs)
    right = sum(exs)
    while left < right:
        me = (left + right) // 2
        if valid(me):
            right = me
        else:
            left = me + 1
    print(right)
    return


q4()