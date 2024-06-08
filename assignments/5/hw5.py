class Tree:
    def __init__(self, node, leaves=None):
        self.node = node
        self.leaves = [] if leaves is None else leaves

    def height(self):
        return max([0] + [Tree.height(leaf) for leaf in self.leaves]) + 1


def q1():
    n = int(input())
    if n == 0:
        print('-1 0')
        return
    leaf_nodes = 0
    parents = [False for _ in range(n)] + [True]
    nodes = [Tree(i) for i in range(n)] + [Tree(-1)]

    for i in range(n):
        left, right = map(int, input().split())
        leaves = [left, right]
        if leaves == [-1, -1]:
            leaf_nodes += 1
            leaves = []
        elif -1 in leaves:
            leaf = (-1) * leaves[0] * leaves[1]
            leaves = [leaf]
        for j in leaves:
            nodes[j].leaves = leaves

    root = parents.index(False)
    print(f'{Tree.height(nodes[root])-1} {leaf_nodes}')
    return


def q2():
    def parse():
        s = []
        nodes = []
        raw = input()
        for c in raw:  # character
            if c not in ['(', ')', ',']:
                s.append(Tree(c))
            elif c != ')':
                s.append(c)
            else:
                l = []  # leaves
                while len(s) > 2 and s[-1] != '(':
                    top = s.pop()
                    if top != ',':
                        l.append(top)
                s.pop()  # '('
                node = s.pop()
                node.leaves = l[::-1]
                s.append(node)
        return s[0]

    def preorder(t):
        pre = t.node
        for leaf in t.leaves:
            pre += preorder(leaf)
        return pre

    def postorder(t):
        post = ''
        for leaf in t.leaves:
            post += postorder(leaf)
        post += t.node
        return post

    t = parse()
    print(preorder(t))
    print(postorder(t))
    return


class File(Tree):
    def __init__(self, node, leaves=None):
        super().__init__(node, leaves)
        self.depth = 0


class Dir(Tree):
    def __init__(self, node, leaves=None):
        super().__init__(node, leaves)
        self.depth = 0


def q3():
    re = ''  # result
    ds_num = 1
    s = [Dir('ROOT')]

    def d_c(t, p_d=0):  # depth_calculate; parent_depth
        for leaf in t.leaves:
            c_d = 1 + p_d  # current_depth
            leaf.depth += c_d
            d_c(leaf, c_d)

    def printer(t):
        nonlocal re
        re += '|     ' * t.depth + t.node + '\n'
        for leaf in t.leaves:
            printer(leaf)

    while True:
        inp = input()
        if inp == '#':
            print(re[:-1])
            return

        if inp == '*':
            re += f'DATA SET {ds_num}:\n'
            l_d = [leaf for leaf in s if isinstance(leaf, Dir)][::-1]
            l_f = [leaf for leaf in s if isinstance(leaf, File)][::-1]
            s = l_d + sorted(l_f, key=lambda x: x.node)
            for t in s:
                d_c(t)
            for t in s:
                printer(t)
            re += '\n'
            ds_num += 1
            s = [Dir('ROOT')]

        else:
            if inp[0] == 'f':
                s.append(File(inp))
            if inp[0] == 'd':
                s.append(Dir(inp))
            if inp == ']':
                l = []
                while not isinstance(s[-1], Dir):
                    l.append(s.pop())
                l.append(s.pop())
                for i in range(len(s)-1, -1, -1):
                    if isinstance(s[i], Dir):
                        l_d = [leaf for leaf in l if isinstance(leaf, Dir)][::-1]
                        l_f = [leaf for leaf in l if isinstance(leaf, File)][::-1]
                        s[i].leaves += l_d + sorted(l_f, key=lambda x: x.node)
                        break


class Uc:
    def __init__(self, node):  # uppercase and lowercase
        self.node = node
        self.left = 0
        self.right = 0

    @property
    def filled(self):
        return self.left != 0 and self.right != 0


class Lc:
    def __init__(self, node):
        self.node = node
        self.filled = True


def q4():
    def convert(pi):  # post_input
        pi = pi[::-1]
        s = []
        for i in pi:
            if 'A' <= i <= 'Z':
                s.append(Uc(i))
            else:
                s.append(Lc(i))
                while len(s) > 1 and s[-1].filled and s[-2].filled:
                    second = s.pop()
                    first = s.pop()
                    operator = s.pop()
                    operator.left, operator.right = first, second
                    s.append(operator)

        t = s[0]
        results = []
        leaves = [t]
        while leaves:
            next_lvs = []
            re = ''
            for c_t in leaves:
                re += c_t.node
                if isinstance(c_t, Uc):
                    next_lvs.append(c_t.left)
                    next_lvs.append(c_t.right)
            results.append(re)
            leaves = next_lvs[:]
        print(''.join(results[::-1]))

    for _ in range(int(input())):
        convert(input())


class Btree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


def q5():
    def build(ino, post):
        if not ino and not post:
            return None

        root = post[-1]
        root_idx = ino.index(root)
        tree = Btree(root)
        left_ino = ino[:root_idx]
        tree.left = build(left_ino, post[:len(left_ino)])
        tree.right = build(ino[root_idx+1:], post[len(left_ino):-1])
        return tree

    re = ''

    def pre(t):
        nonlocal re
        if t:
            re += t.node
            pre(t.left)
            pre(t.right)

    ino = input()
    post = input()
    pre(build(ino, post))
    print(re)
    return


def q6():
    def build(ino, pre):
        if not ino and not pre:
            return None

        root = pre[0]
        root_idx = ino.index(root)
        tree = Btree(root)
        left_ino = ino[:root_idx]
        tree.left = build(left_ino, pre[1:len(left_ino)+1])
        tree.right = build(ino[root_idx+1:], pre[len(left_ino)+1:])
        return tree

    re = ''

    def post(t):
        nonlocal re
        if t:
            post(t.left)
            post(t.right)
            re += t.node


    while True:
        try:
            pre = input()
            if not pre: return
            ino = input()
            post(build(ino, pre))
            print(re)
            re = ''
        except EOFError:
            return


q6()