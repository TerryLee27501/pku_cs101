# Assignment #D: May月考

Updated 1654 GMT+8 May 8, 2024

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

### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：5 mins.



代码

```python
def q1():
    l, m = map(int, input().split())
    s = set(range(0, l+1))
    for _ in range(m):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            if i in s:
                s.remove(i)
    print(len(s))


q1()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240514230522185](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240514230522185.png)



### 20449: 是否被5整除

http://cs101.openjudge.cn/practice/20449/



思路：7 mins.



代码

```python
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


q2()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240514231314442](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240514231314442.png)



### 01258: Agri-Net

http://cs101.openjudge.cn/practice/01258/



思路：17 mins.



代码

```python
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


q3()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240520194902885](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240520194902885.png)



### 27635: 判断无向图是否连通有无回路(同23163)

http://cs101.openjudge.cn/practice/27635/



思路：15 mins if without compile errors.



代码

```python
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240520224440628](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240520224440628.png)





### 27947: 动态中位数

http://cs101.openjudge.cn/practice/27947/



思路：限时内没有做出来，因为当时用了pop而非指针导致一直超时。



代码

```python
import heapq

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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 28190: 奶牛排队

http://cs101.openjudge.cn/practice/28190/



思路：



代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

pop比指针耗时更大；oj上用# pylint: skip-file跳过静态测试。



