# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by 李鹏辉，元培学院



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

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

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：约30分钟。



##### 代码

```python
def reduce(a, b):
    min_num = min(a, b)
    for k in range(2, min_num+1):
        if a % k == 0 and b % k == 0:
            return reduce(a//k, b//k)
    return a, b


class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def to_add(self, another):
        num = self.num * another.den + self.den * another.num
        den = self.den * another.den
        self.num, self.den = reduce(abs(num), abs(den))
        if num < 0: self.num = -self.num
        if den < 0: self.den = -self.den

    def __str__(self):
        return f'{self.num}/{self.den}'


num_list = input().split()
first_fraction = Fraction(int(num_list[0]), int(num_list[1]))
second_fraction = Fraction(int(num_list[2]), int(num_list[3]))
first_fraction.to_add(second_fraction)
print(first_fraction)
```



代码运行截图

![image-20240228192152896](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240228192152896.png)



### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：约50分钟。最后打印时一开始未采用格式化输出，而是使用round函数。



##### 代码

```python
def q2_parser():
    sort, max_weight = map(int, input().split())
    candies = []
    for _ in range(sort):
        value, weight = map(int, input().split())
        candies.append([value/weight, value, weight])
    candies.sort(key=lambda x: x[0], reverse=True)
    return max_weight, candies


def value_calculator(max_weight, candies):
    total_value = 0
    total_weight = 0
    for candy in candies:
        if max_weight > total_weight:
            if max_weight >= total_weight + candy[2]:
                total_value += candy[1]
                total_weight += candy[2]
            else:
                total_value += candy[0] * (max_weight - total_weight)
                break
        else: break
    return total_value


print("{:.1f}".format(value_calculator(*q2_parser())))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240304175805565](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240304175805565.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：约1小时。最开始没有用埃氏筛法导致超时，换到第6题看到提示后全部重写。



##### 代码

```python
import math
 
def sieve(n):
    sieve_list = [False, False] + [True] * (n - 1)
    for i in range (2, int(n**0.5)):
        if sieve_list[i]:
            for j in range(i*i, n+1, i):
                sieve_list[j] = False
    return sieve_list
 
 
sieve_list = sieve(1000000)
ignored = input()
nums = map(int, input().split())
for i in nums:
    print('YES' if math.sqrt(i) == int(math.sqrt(i)) and sieve_list[int(math.sqrt(i))] else 'NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240304175904130](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240304175904130.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：



##### 代码

```python
# 

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：在第4题的基础上再多花约20分钟。



##### 代码

```python
import math

def sieve(n):
    sieve_list = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n))):
        if sieve_list[i]:
            for j in range(i*i, n+1, i):
                sieve_list[j] = False
    return sieve_list


def is_T_prime(i):
    if i < 4:
        return False
    if math.sqrt(i) == int(math.sqrt(i)) and sieve_list[int(math.sqrt(i))]:
        return True
    return False


def average_calculate(scores):
    total = 0
    for score in scores:
        if is_T_prime(score):
            total += score
    if total == 0: return 0
    return "{:.2f}".format(total / len(scores))


sieve_list = sieve(10000)
students_num = int(input().split()[0])
for _ in range(students_num):
    scores = list(map(int, input().split()))
    print(average_calculate(scores))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240304175951117](C:\Users\lph\AppData\Roaming\Typora\typora-user-images\image-20240304175951117.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

第2题在输出细节上花费了大量时间，之后要更精确地理解题目的输出要求，如果读不懂就直接看答案的输出方式好了。第4题与第6题的一脉相承再次说明了写函数的重要性！



