# Assignment #4: 排序、栈、队列和树

Updated 0005 GMT+8 March 11, 2024

2024 spring, Complied by ==李鹏辉，元培学院==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:

Learn about Time complexities, learn the basics of individual Data Structures, learn the basics of Algorithms, and practice Problems.

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==Windows 10 Home, PyCharm 2022.3.2 (Community Edition)==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 05902: 双端队列

http://cs101.openjudge.cn/practice/05902/



思路：10分钟。



代码

```python
def q1():
    for _ in range(int(input())):
        s = []
        for _ in range(int(input())):
            op, num = tuple(map(int, input().split()))
            if op == 1:
                s.append(num)
            elif s:
                if num == 0:
                    s.pop(0)
                else:
                    s.pop()
            else:
                break
        if s:
            print(' '.join(map(str, s)))
        else:
            print('NULL')


q1()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240319130525215](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240319130525215.png)



### 02694: 波兰表达式

http://cs101.openjudge.cn/practice/02694/



思路：15分钟。



代码

```python
import operator as op


def q2():
    chars = input().split()
    s = []
    op_d = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    for char in chars:
        if char in op_d:
            s.append(char)
        else:
            s.append(float(char))
            while len(s) > 2 and s[-2] not in op_d:
                second = s.pop()
                first = s.pop()
                s.append(op_d[s.pop()](first, second))
    return s[0]


print(format(q2(), '.6f'))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240319175725276](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240319175725276.png)



### 24591: 中序表达式转后序表达式

http://cs101.openjudge.cn/practice/24591/



思路：改良了一下课件上的调度场，数字不需要转换成int或float。一小时。



代码

```python
def q3():
    prec = {'+':1, '-':1, '*':2, '/':2}

    for _ in range(int(input())):
        infix = input()
        s = []
        re = []
        num = ''

        for char in infix:
            if char.isnumeric() or char == '.':
                num += char
            else:
                if num:
                    re.append(num)
                    num = ''
                if char == '(':
                    s.append(char)
                if char == ')':
                    while s and s[-1] != '(':
                        re.append(s.pop())
                    s.pop()
                if char in '+-*/':
                    while s and s[-1] in '+-*/' and prec[char] <= prec[s[-1]]:
                        re.append(s.pop())
                    s.append(char)

        if num:
            re.append(num)
        while s:
            re.append(s.pop())
        print(' '.join(str(x) for x in re))


q3()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240319230248224](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240319230248224.png)



### 22068: 合法出栈序列

http://cs101.openjudge.cn/practice/22068/



思路：主要改变输入的字符串去匹配原来的字符串，40分钟。



代码

```python
def q4():
    chars = input()
    while True:
        try:
            wait = input()
            if len(wait) != len(chars):
                print('NO')
                continue
            c_r = chars[:]  # chars_remained
            fixed = ''
            while wait:
                f_l = wait[0]  # first_letter
                if f_l not in chars:
                    print('NO')
                    break
                elif f_l not in fixed:
                    f_i = c_r.index(f_l)  # first_index
                    fixed += c_r[:f_i]
                    c_r = c_r[f_i+1:]
                elif f_l == fixed[-1]:
                    fixed = fixed[:-1]
                else:
                    print('NO')
                    break
                wait = wait[1:]
            if not wait:
                print('YES')
        except EOFError:
            break


q4()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 06646: 二叉树的深度

http://cs101.openjudge.cn/practice/06646/



思路：bfs. 15分钟。



代码

```python
def q5():
    t_d = {}  # tree_dict
    for _ in range(int(input())):
        t_d[_+1] = list(map(int, input().split()))
    m_d = 0  # max_depth
    n_q = [1]  # node_queue
    while n_q:
        m_d += 1
        n_q_c = n_q[:]  # n_q_copy
        n_q = []
        for node in n_q_c:
            for leave in t_d[node]:
                if leave != -1:
                    n_q.append(leave)
    return m_d


print(q5())
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240319200730759](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240319200730759.png)



### 02299: Ultra-QuickSort

http://cs101.openjudge.cn/practice/02299/



思路：一开始只用sorted排序，后来发现超时。经提醒改用merge sort和栈，最后总计约两小时。



代码

```python
def q6():

    while True:
        size = int(input())
        if size == 0:
            break
        numbers = [int(input()) for _ in range(size)]
        s = [numbers[:size//2], numbers[size//2:]]
        result = []
        times = 0

        def merge(l1, l2):
            nonlocal times
            re = []
            while l1 and l2:
                if l1[0] <= l2[0]:
                    re.append(l1.pop(0))
                else:
                    re.append(l2.pop(0))
                    times += len(l1)
            if l1:
                re += l1
            if l2:
                re += l2
            return re

        while s:
            top = s.pop()
            t_s = len(top)
            if t_s > 1:
                s.append(top[:t_s//2])
                s.append(top[t_s//2:])
            else:
                c_l = top
                while result and len(result[-1]) == len(c_l):
                    c_l = merge(result.pop(), c_l)
                result.append(c_l)
        while len(result) > 1:
            l2 = result.pop()
            l1 = result.pop()
            result.append(merge(l1, l2))
        print((size * size - size) // 2 - times)


q6()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240319221500089](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240319221500089.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

第四题其实如果换种思路，改成通过改变原来的字符串去匹配新输入的字符串，会方便很多。第六题应该对大数足够敏感到能意识到要用归并。



