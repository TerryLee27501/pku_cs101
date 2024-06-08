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
