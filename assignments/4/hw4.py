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


#print(format(q2(), '.6f'))


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


def q4():
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


q4()
