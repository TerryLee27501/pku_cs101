# Assignment #F: All-Killed 满分

Updated 1844 GMT+8 May 20, 2024

2024 spring, Complied by ==李鹏辉，元培学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==Windows 10 Home, PyCharm 2022.3.2 (Community Edition)==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 22485: 升空的焰火，从侧面看

http://cs101.openjudge.cn/practice/22485/



思路：12 mins.



代码

```python
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


q1()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240521231848142](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240521231848142.png)



### 28203:【模板】单调栈

http://cs101.openjudge.cn/practice/28203/



思路：看题解才做出来的，就当学模板吧。



代码

```python
def q2():
    n = int(input())
    ns = [0] + list(map(int, input().split()))
    s = []
    for i in range(1, 1+n):
        while s and ns[s[-1]] < ns[i]:
            ns[s.pop()] = i
        s.append(i)
    while s:
        ns[s.pop()] = 0
    print(' '.join(map(str, ns[1:])))
    return


q2()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240522002424415](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240522002424415.png)



### 09202: 舰队、海域出击！

http://cs101.openjudge.cn/practice/09202/



思路：24 mins.



代码

```python
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


q3()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240522005634720](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240522005634720.png)



### 04135: 月度开销

http://cs101.openjudge.cn/practice/04135/



思路：



代码

```python
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 07735: 道路

http://cs101.openjudge.cn/practice/07735/



思路：学完动态规划及背包问题后才做出来的。



代码

```python
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


q5()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240524110017243](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240524110017243.png)



### 01182: 食物链

http://cs101.openjudge.cn/practice/01182/



思路：20 mins.



代码

```python
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


q6()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240524105955726](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240524105955726.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

其中有相当一部分题目考的就是是否之前做过类似的题目，比如单调栈和动态规划。所以要多刷题。



