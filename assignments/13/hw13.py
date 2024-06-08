def q1():
    l, m = map(int, input().split())
    s = set(range(0, l+1))
    for _ in range(m):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            if i in s:
                s.remove(i)
    print(len(s))


def q2():
    s = [int(i) for i in input()]
    re = ''
    for i in range(len(s)):
        ten = 0
        for j in range(i+1):
            ten += s[j] * (2 ** (i-j))
        if not ten % 5:
            re += '1'
        else:
            re += '0'
    print(re)


import heapq


def q3():
    try:
        while True:
            n = int(input())
            g = []
            for i in range(n):
                ds = list(map(int, input().split()))
                g.append(ds)
            v = [False] * n
            ds = [100001] * n
            q = []
            heapq.heappush(q, (0, 0))
            ds[0] = 0
            while q:
                d, cv = heapq.heappop(q)
                if v[cv]: continue
                v[cv] = True
                for i in range(n):
                    if v[i]: continue
                    if g[cv][i] < ds[i]:
                        ds[i] = g[cv][i]
                        heapq.heappush(q, (ds[i], i))
            print(sum(ds))

    except EOFError:
        return


def q4():
    n, m = map(int, input().split())
    ps = []
    for j in range(n):
        ps.append(j)

    def find(i):
        if ps[i] != i:
            ps[i] = find(ps[i])
        return ps[i]

    def union(x, y):
        ps[find(x)] = find(y)

    l = False
    for _ in range(m):
        x, y = map(int, input().split())
        if find(x) == find(y):
            l = True
        else:
            union(x, y)
    ps = [find(i) for i in range(n)]
    ps = set(ps)
    print('connected:yes' if len(ps) == 1 else 'connected:no')
    print('loop:yes' if l else 'loop:no')


def q5():
    n = int(input())
    for _ in range(n):
        ns = list(map(int, input().split()))
        cm = ns[0]
        re = [ns[0]]
        lt = []
        mt = []
        i = 1
        heapq.heappush(mt, cm)
        balance = 1

        while len(ns) - i > 1:
            a = ns[i]
            b = ns[i+1]
            x = min(a, b)
            y = max(a, b)
            if x > cm:
                heapq.heappush(mt, x)
                heapq.heappush(mt, y)
                if balance == 1:
                    heapq.heappush(lt, -heapq.heappop(mt))
                balance = 1
                cm = mt[0]
            elif y < cm:
                heapq.heappush(lt, -x)
                heapq.heappush(lt, -y)
                if balance == -1:
                    heapq.heappush(mt, -heapq.heappop(lt))
                balance = -1
                cm = -lt[0]
            else:
                heapq.heappush(lt, -x)
                heapq.heappush(mt, y)
            re.append(cm)
            i += 2
        print(len(re))
        print(' '.join(map(str, re)))
    return


class Sets:
    def __init__(self, n, hs):
        self.size = n
        self.pts = []
        self.hs = hs
        self.ls = 0  # largest span

    def check_point(self, l):
        i = 0
        while self.pts[i][0] < l:
            i += 1
        if self.pts[i][1] == 'end':
            return
        else:
            rm = self.pts[i][0]
            if rm - l <= self.ls: return
            r = self.find_right_point(l, rm)
            if r == -1: return
            self.pts.insert(i, (l, 'start'))
            self.pts.insert(i, (r, 'end'))
            if r - l > self.ls: self.ls = r - l

    def find_right_point(self, l, rm):
        for i in range(self.size-1, -1, -1):
            if



def ms(arr):
    if len(arr) > 1:
        m = arr // 2
        l = arr[:m]
        r = arr[m:]
        l = ms(l)
        r = ms(r)
        i, j = 0, 0
        re = []
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                re.append(l[i])
                i += 1
            elif l[i] > r[j]:
                re.append(r[j])
                j += 1
            else:
                re.append(l[i])
                re.append(l[i])
                i += 1
                j += 1
        if i < len(l):
            re.extend(l[i:])
        if j < len(r):
            re.extend(j[r:])
        return re
    else: return arr


def q6():
    n = int(input())
    hs = []
    for i in range(n):
        h = int(input())
        hs.append((h, i))
    shs = ms(hs)
    mh = 0
    op = {}
    for i in range(n):
        if i in op: continue
        if shs[i][0] == shs[i+1][0]: continue
