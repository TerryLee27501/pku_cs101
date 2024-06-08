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