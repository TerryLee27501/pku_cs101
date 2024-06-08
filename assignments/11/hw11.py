def q1():
    places = {}
    for x in range(10):
        string = input()
        for y in range(10):
            if string[y] == '.':
                places[(x, y)] = ''

    result = 0
    visited = {}

    def helper(x, y):
        visited[(x, y)] = ''
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            new_place = (x+dx, y+dy)
            if new_place in places and new_place not in visited:
                helper(x+dx, y+dy)

    for x, y in places.keys():
        if (x, y) not in visited:
            helper(x, y)
            result += 1

    print(result)
    return


def q2():
    def okay(places, num, i):
        for j in range(num):
            if places[j] == i or\
              abs(j-num) == abs(places[j]-i):
                return False
        return True

    s = [[[i+1] + [-1]*7, 1] for i in range(8)]
    re = []
    while s:
        places, num = s.pop()
        if num == 8:
            re.append(''.join(map(str, places)))
        else:
            for i in range(1, 9):
                if okay(places, num, i):
                    np = places[:]
                    np[num] = i
                    s.append([np, num+1])

    re = list(map(int, re))
    re.sort()
    for _ in range(int(input())):
        i = int(input())
        print(re[i-1])
    return


def q3():
    ma, mb, c = map(int, input().split())
    steps_dict = {}
    q = [[(0, 0), []]]
    while q:
        liters, steps = q.pop(0)
        a, b = liters
        if a == c or b == c:
            print(len(steps))
            [print(step) for step in steps]
            return
        if liters in steps_dict:
            continue
        steps_dict[liters] = steps
        if a < ma:
            steps.append('FILL(1)')
            q.append([(ma, b), steps[:]])
            steps.pop()
            if b > 0:
                steps.append('POUR(2,1)')
                if ma - a > b:
                    q.append([(a+b, 0), steps[:]])
                else:
                    q.append([(ma, a+b-ma), steps[:]])
                steps.pop()
        if b < mb:
            steps.append('FILL(2)')
            q.append([(a, mb), steps[:]])
            steps.pop()
            if a > 0:
                steps.append('POUR(1,2)')
                if mb - b > a:
                    q.append([(0, a + b), steps[:]])
                else:
                    q.append([(a + b - mb, mb), steps[:]])
                steps.pop()
        if a > 0:
            steps.append('DROP(1)')
            q.append([(0, b), steps[:]])
            steps.pop()
        if b > 0:
            steps.append('DROP(2)')
            q.append([(a, 0), steps[:]])
            steps.pop()
    print('impossible')
    return


class BTree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None
        self.parent = None


def q4():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        nodes = [BTree(i) for i in range(n)]
        for _ in range(n):
            node, leftnum, rightnum = map(int, input().split())
            if leftnum != -1:
                nodes[node].left = nodes[leftnum]
                nodes[leftnum].parent = nodes[node]
            if rightnum != -1:
                nodes[node].right = nodes[rightnum]
                nodes[rightnum].parent = nodes[node]
        t = nodes[0]

        for _ in range(m):
            nums = list(map(int, input().split()))
            if nums[0] == 2:
                ct = nodes[nums[1]]
                while ct.left is not None:
                    ct = ct.left
                print(ct.node)
            if nums[0] == 1:
                a, b = nums[1:]
                a_parent = nodes[a].parent
                b_parent = nodes[b].parent
                a_dir = 'left' if a_parent.left == nodes[a] else 'right'
                b_dir = 'left' if b_parent.left == nodes[b] else 'right'
                exec('a_parent.' + a_dir + ' = nodes[b]')
                exec('b_parent.' + b_dir + ' = nodes[a]')
                nodes[a].parent = b_parent
                nodes[b].parent = a_parent
    return


def q5():
    while True:
        try:
            n, m = map(int, input().split())
            parents = [0] + [i+1 for i in range(n)]

            def find(a):
                if parents[a] == a:
                    return a
                else:
                    parents[a] = find(parents[a])
                    return parents[a]

            for _ in range(m):
                a, b = map(int, input().split())
                if find(a) == find(b):
                    print('Yes')
                else:
                    print('No')
                    parents[find(b)] = a

            left = []
            for i in range(1, n+1):
                root = find(i)
                if root not in left:
                    left.append(root)
            left.sort()
            print(len(left))
            print(' '.join(map(str, left)))
        except:
            return


import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.connected_to = {}
        self.previous = None
        self.distance = 9999999999


class Graph:
    def __init__(self):
        self.vertices = {}

    def get(self, name):
        return self.vertices[name]

    def add_edge(self, f, t, weight):
        self.get(f).connected_to[self.get(t)] = weight
        self.get(t).connected_to[self.get(f)] = weight


def q6():
    g = Graph()
    n = int(input())
    for _ in range(n):
        name = input()
        g.vertices[name] = Vertex(name)
    n = int(input())
    for _ in range(n):
        a, b, d = input().split()
        d = int(d)
        g.add_edge(a, b, d)
    n = int(input())
    for _ in range(n):
        s, e = input().split()
        c = g.get(s)
        c.distance = 0
        pq = []
        heapq.heappush(pq, (0, c))
        while True:
            if not pq: break
            cd, c = heapq.heappop(pq)
            if c.name == e: break
            for np, d in c.connected_to.items():
                if cd + d < np.distance:
                    np.distance = cd + d
                    np.previous = c
                    heapq.heappush(pq, (np.distance, np))
        re = [e]
        while c != g.get(s):
            last = c.previous
            re.append(f'({c.connected_to[last]})')
            re.append(last.name)
            c = last
        print('->'.join(re[::-1]))
        for vertex in g.vertices.values():
            vertex.previous = None
            vertex.distance = 9999999999
    return


q6()