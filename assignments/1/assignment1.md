# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by 李鹏辉，元培学院



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

Windows 10 Home, PyCharm 2022.3.2 (Community Edition)

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：大概8分钟。



##### 代码

```python
def tbnc(n):
    if n == 1 or n == 2: return 1
    else:
        tbnc_list = [0, 1, 1]
        while n >= len(tbnc_list):
            tbnc_list.append(tbnc_list[-3] + tbnc_list[-1] + tbnc_list[-2])
        return tbnc_list[n]


k = int(input())
print(tbnc(k))
```



代码运行截图

![48314ffefdbf1a0953e788d112ba36d](C:\Users\lph\Documents\WeChat Files\wxid_104h8p9u3p5n22\FileStorage\Temp\48314ffefdbf1a0953e788d112ba36d.png)



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：



##### 代码

```python
```



代码运行截图 ==（至少包含有"Accepted"）==





### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：大概15分钟。



##### 代码

```python
import math


def is_prime(n):
    if n == 2 or n == 3: return True
    range_max = int(math.sqrt(n))
    for i in range(2, range_max+1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    if n % 2 == 1 or n == 4:
        first = 2
    else:
        for i in range(3, n//2+1):
            if is_prime(i) and is_prime(n-i):
                first = i
                break
    print(f'{first} {n-first}')


k = int(input())
goldbach(k)
```



代码运行截图 

![8bfc0b49d33c5b340fa23e9a67de127](C:\Users\lph\Documents\WeChat Files\wxid_104h8p9u3p5n22\FileStorage\Temp\8bfc0b49d33c5b340fa23e9a67de127.png)



### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：大概25分钟。



##### 代码

```python
def poly_split(poly):
    if '+' not in poly: return [poly]
    else: return poly.split('+')


def mono_compare(mono_list):
    index_list = []
    for mono in mono_list:
        if mono.startswith('0') or '^' not in mono:
            index_list.append(0)
        else:
            index_list.append(int(mono[mono.index('^')+1:]))
    return max(index_list)


k = input()
print(f'n^{mono_compare(poly_split(k))}')
```



代码运行截图 

![49a0a273ad38b75d5d31f6d22e60eae](C:\Users\lph\Documents\WeChat Files\wxid_104h8p9u3p5n22\FileStorage\Temp\49a0a273ad38b75d5d31f6d22e60eae.png)





### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：大概40分钟。



##### 代码

```python
def votes_count(votes):
    votes_list = votes.split(' ')
    votes_dict = {}
    for vote in votes_list:
        if vote not in votes_dict:
            votes_dict[vote] = 1
        else:
            votes_dict[vote] += 1
    options, max_number = [], 0
    for option, number in votes_dict.items():
        if number > max_number:
            max_number = number
            options = [int(option)]
        elif number == max_number:
            options.append(int(option))
    options.sort()
    result = ''
    for option in options:
        result += str(option) + ' '
    print(result[:-1])


votes_count(input())
```



代码运行截图 

![db81fc5a2c6e73367d8098692db3cec](C:\Users\lph\Documents\WeChat Files\wxid_104h8p9u3p5n22\FileStorage\Temp\db81fc5a2c6e73367d8098692db3cec.png)





## 2. 学习总结和收获

做比较复杂的题目前先罗列好可能的各种情况。另外使用字典计数比列表更快。





