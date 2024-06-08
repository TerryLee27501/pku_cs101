# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

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

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：1 min.



代码

```python
words = input().split()
print(' '.join(map(str, words[::-1])))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240404210736734](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404210736734.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：8 mins.



代码

```python
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
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240404211514012](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404211514012.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：8 mins.



代码

```python
n, k = map(int, input().split())
num_list = [1] + sorted(list(map(int, input().split()))) + [-2]
print(num_list[k] if num_list[k] != num_list[k+1] else -1)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240404212316339](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404212316339.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：13 mins.



代码

```python
class BTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def classify(r_str):
    if '0' in r_str:
        return 'F' if '1' in r_str else 'B'
    else:
        return 'I'


def build(r_str):
    t = BTree(classify(r_str))
    if len(r_str) == 1:
        return t
    else:
        half = len(r_str) // 2
        left_str = r_str[:half]
        right_str = r_str[half:]
        t.left = build(left_str)
        t.right = build(right_str)
        return t


re = ''


def preorder(t):
    global re
    if t.left:
        preorder(t.left)
        preorder(t.right)
    re += t.value


input()
t = build(input())
preorder(t)
print(re)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240404213550665](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404213550665.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：21 mins.



代码

```python
t = int(input())
members = [0] * 1000000
teams = [[] for _ in range(t)]
team_order = []
for i in range(t):
    team_members = list(map(int, input().split()))
    for member in team_members:
        members[member] = i


def enqueue(member):
    team = members[member]
    teams[team].append(member)
    if team not in team_order:
        team_order.append(team)


def dequeue():
    first_team = team_order[0]
    print(teams[first_team].pop(0))
    if not teams[first_team]:
        team_order.pop(0)


while True:
    raw = input()
    if raw[0] == 'E':
        enqueue(int(raw[8:]))
    elif raw[0] == 'D':
        dequeue()
    else:
        break
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240404215713374](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404215713374.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：大约1小时。主要难点在于建树，首先尝试用第五周作业的方法设两个list，超过内存后只能改用字典存储节点并用逻辑判断的方式更新parent。



代码

```python
class Tree:
    def __init__(self, value, leaves=None):
        self.value = value
        self.leaves = [] if leaves is None else leaves


def printer(t):
    if not t.leaves:
        print(t.value)
        return
    else:
        less = [l for l in t.leaves if l.value < t.value]
        if less:
            less.sort(key=lambda x: x.value)
        more = [l for l in t.leaves if l.value > t.value]
        if more:
            more.sort(key=lambda x: x.value)
        for l in less:
            printer(l)
        print(t.value)
        for l in more:
            printer(l)


n = int(input())
node_dict = {}
no_parent = []
for _ in range(n):
    num_list = list(map(int, input().split()))
    if num_list[0] not in node_dict:
        no_parent.append(num_list[0])
    for num in num_list:
        if num not in node_dict:
            node_dict[num] = Tree(num)
        else:
            if num in no_parent:
                no_parent.remove(num)
    node_dict[num_list[0]].leaves = [node_dict[num] for num in num_list[1:]]
t = node_dict[no_parent[0]]
printer(t)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240404225456131](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240404225456131.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

遍历树是很好的举一反三的例子：首先要回想到第五周作业第二题，想到用一个变量储存所有节点，一个parent变量储存是否有父节点；其次要根据此题特殊状况改变实现方式，因为数据过大且不是从0开始连续编号，因此照搬使用列表不现实，只能用字典储存节点，将parent变量的含义从“是否有父节点”变为“可能有父节点”。



