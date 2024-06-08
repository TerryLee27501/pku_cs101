n, m = map(int, input().split())
p = [i for i in range(n)]

def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]

def union(x, y):
    p[find(x)] = find(y)

l = False
for _ in range(m):
    x, y = map(int, input().split())
    if find(x) == find(y):
        l = True
    else:
        union(x, y)
p = [find(i) for i in range(n)]
p = set(p)
print('connected:yes' if len(p) == 1 else 'connected:no')
print('loop:yes' if l else 'loop:no')