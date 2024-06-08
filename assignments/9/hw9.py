class Tree:
    def __init__(self, node):
        self.node = node
        self.children = []
        self.parent = None
        self.depth = 0
        self.new_depth = 0


def q1():
    dus = input()
    t = Tree(0)
    c_node = t  # current_node
    c_number = 0
    m_d_b = 0  # max_depth_before
    for _, i in enumerate(dus):
        if i == 'd':
            c_number += 1
            c_node.children.append(Tree(c_number))
            c_node.children[-1].parent = c_node
            c_node.children[-1].depth = c_node.depth + 1
            c_node = c_node.children[-1]
            if c_node.depth > m_d_b:
                m_d_b = c_node.depth
        else:
            c_node = c_node.parent
    q = [t]
    m_d_a = 0  # max_depth_after
    while q:
        root = q.pop(0)
        for i, n in enumerate(root.children):
            n.new_depth = root.new_depth + i + 1
            if n.new_depth > m_d_a:
                m_d_a = n.new_depth
            q.append(n)
    print(f'{m_d_b} => {m_d_a}')


class BTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


def q2():
    def build_tree(r):
        cs = r[1:]  # current string
        t = BTree(r[0])
        s = [t]
        while cs:
            nt = BTree(cs[0])  # new tree
            cs = cs[1:]
            if s[-1].left is None:
                s[-1].left = nt
                if nt.node != '.':
                    s.append(nt)
            else:
                s[-1].right = nt
                s.pop()
                if nt.node != '.':
                    s.append(nt)
        return t

    def inorder(t):
        re = ''
        if t.left.node != '.':
            re += inorder(t.left)
        re += t.node
        if t.right.node != '.':
            re += inorder(t.right)
        return re

    def postorder(t):
        re = ''
        if t.left.node != '.':
            re += postorder(t.left)
        if t.right.node != '.':
            re += postorder(t.right)
        re += t.node
        return re

    t = build_tree(input())
    print(inorder(t))
    print(postorder(t))


def q3():
    ms = []  # min stack
    cm = -1  # current min
    ws = []  # weight stack
    try:
        while True:
            o = input()
            if o == 'min':
                if cm == -1:
                    continue
                else:
                    print(cm)

            if o.startswith('push'):
                _, w = o.split()
                w = int(w)
                ws.append(w)
                if w <= cm or cm == -1:
                    cm = w
                    ms.append(w)

            if o == 'pop':
                if cm == -1:
                    continue
                else:
                    top = ws.pop()
                    if top == cm:
                        ms.pop()
                        if ms:
                            cm = ms[-1]
                        else:
                            cm = -1

    except EOFError:
        return


class Point:
    def __init__(self, ors):
        self.ors = ors
        self.suns = []
        self.av = True


def q4():
    def build_graph(n, m):
        pd = {}  # points_dict
        for i in range(0, n):
            for j in range(0, m):
                pd[(i, j)] = Point((i, j))

        dirs = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
        for i in range(0, n):
            for j in range(0, m):
                suns = []
                for direction in dirs:
                    xm, ym = direction
                    if 0 <= i+xm <= n-1 and 0 <= j+ym <= m-1:
                        suns.append((i+xm, j+ym))
                pd[(i, j)].suns.extend([pd[sun] for sun in suns])
        return pd

    for _ in range(int(input())):
        il = map(int, input().split())  # input split
        n, m, x, y = il
        pd = build_graph(n, m)
        fl = n * m  # full length
        apps = 0

        def dfs(ap, pl):  # aim point, past length
            nonlocal apps
            if pl == fl - 1:
                apps += 1
            else:
                ap.av = False
                for ps in ap.suns:  # possible 'sun'
                    if ps.av:
                        dfs(ps, pl+1)
                ap.av = True

        dfs(pd[(x, y)], 0)
        print(apps)


class Word:
    def __init__(self, word):
        self.node = word
        self.nbrs = []
        self.av = True
        self.prev = None


def q5():
    def build_graph():
        wd = {}  # word dict
        for _ in range(int(input())):
            w = input()
            wd[w] = Word(w)

        wmd = {}  # word model dict
        for w in wd.keys():
            for i in range(4):
                m = w[:i] + '_' + w[i+1:]  # model
                if m in wmd:
                    wmd[m].append(wd[w])
                else:
                    wmd[m] = [wd[w]]
        for m in wmd.values():
            for w in m:
                for ow in m:  # other words
                    if ow != w:
                        w.nbrs.append(ow)
        return wd

    wd = build_graph()
    start, des = input().split()
    if start not in wd.keys() or des not in wd.keys():
        print('NO')
        return
    wd[start].av = False
    q = [wd[start]]

    while q:
        aw = q.pop(0)
        if aw.node == des:
            rl = [des]  # result list
            cw = aw.prev  # current word
            while cw is not None:
                rl.append(cw.node)
                cw = cw.prev
            print(' '.join(rl[::-1]))
            return
        else:
            for w in aw.nbrs:
                if w.av:
                    w.av = False
                    w.prev = aw
                    q.append(w)
    print('NO')
    return


import sys


class Point:
    def __init__(self, ors):
        self.ors = ors
        self.suns = []
        self.av = True


def q6():
    def build_graph(n, m):
        pd = {}  # points_dict
        for i in range(0, n):
            for j in range(0, m):
                pd[(i, j)] = Point((i, j))

        dirs = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
        for i in range(0, n):
            for j in range(0, m):
                suns = []
                for direction in dirs:
                    xm, ym = direction
                    if 0 <= i+xm <= n-1 and 0 <= j+ym <= m-1:
                        suns.append((i+xm, j+ym))
                pd[(i, j)].suns.extend([pd[sun] for sun in suns])
        return pd

    n = int(input())
    il = map(int, input().split())  # input split
    x, y = il
    pd = build_graph(n, n)
    fl = n * n  # full length

    def dfs(ap, pl):  # aim point, past length
        if pl == fl - 1:
            print('success')
            sys.exit(0)
        else:
            ap.av = False
            ps = []
            for s in ap.suns:  # possible 'sun'
                if s.av:
                    sps = 0  # the sun's possible suns
                    for ss in s.suns:  # suns of the sun
                        if ss.av:
                            sps += 1
                    ps.append([s, sps])
            ps.sort(key=lambda x: x[1])
            for s in ps:
                dfs(s[0], pl+1)
            ap.av = True

    dfs(pd[(x, y)], 0)
    print('fail')


q6()