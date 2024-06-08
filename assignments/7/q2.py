times = 0
q = []
size = 0
s_m, n = map(int, input().split())
w_l = list(map(int, input().split()))
for w in w_l:
    if w not in q:
        times += 1
        if size < s_m:
            q.append(w)
            size += 1
        else:
            q.pop(0)
            q.append(w)
print(times)