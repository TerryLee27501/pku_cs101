n, k = map(int, input().split())
num_list = [1] + sorted(list(map(int, input().split()))) + [-2]
print(num_list[k] if num_list[k] != num_list[k+1] else -1)