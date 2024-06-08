def intercept(upper_bound, heights):
    possible_heights = [height for height in heights if height <= upper_bound]
    if len(possible_heights) == 1:
        return 1
    if len(possible_heights) == 0:
        return 0
    return max(1+intercept(possible_heights[0], possible_heights[1:]), intercept(upper_bound, heights[1:]))


def q1():
    ignore = input()
    heights = list(map(int, input().split()))
    print(intercept(1000000000, heights))


def hanoi(n, source, target, bridge):
    if n == 1:
        print(f"1:{source}->{target}")
        return
    else:
        hanoi(n-1, source, bridge, target)
        print(f"{n}:{source}->{target}")
        hanoi(n-1, bridge, target, source)
        return


def q2():
    raw_list = input().split()
    hanoi(int(raw_list[0]), raw_list[1], raw_list[3], raw_list[2])


def joseph(n, p, m):
    players = list(range(1, n+1))
    index = p - 1
    result = ''
    while len(players) > 1:
        index += m - 1
        index %= len(players)
        deleted = players.pop(index)
        result += str(deleted) + ','
    result += str(players[0])
    print(result)


def q3():
    while True:
        raw_string = input()
        if raw_string == '0 0 0':
            break
        inputs = tuple(map(int, raw_string.split()))
        joseph(*inputs)

'''
while True:
    n, p, m = map(int, input().split())
    if {n,p,m} == {0}:
        break
    monkey = [i for i in range(1, n+1)]
    for _ in range(p-1):
        tmp = monkey.pop(0)
        monkey.append(tmp)
    # print(monkey)

    index = 0
    ans = []
    while len(monkey) != 1:
        temp = monkey.pop(0)
        index += 1
        if index == m:
            index = 0
            ans.append(temp)
            continue
        monkey.append(temp)

    ans.extend(monkey)

    print(','.join(map(str, ans)))
    '''


def q4():
    n = int(input())
    times = list(map(int, input().split()))
    for i in range(1, n+1):
        times[i-1] = [times[i-1], i]
    times.sort(key=lambda x: x[0])
    order = []
    sum_result = 0
    for j in range(1, n+1):
        order.append(times[j-1][1])
        sum_result += (n - j) * times[j-1][0]
    print(' '.join(map(str, order)))
    print("{:.2f}".format(sum_result / n))


def q6():
    n = int(input())
    model_dict = {}
    ori_mb = "{'M':[], 'B':[]}"
    for _ in range(n):
        model, size = tuple(input().split('-'))
        if model not in model_dict:
            model_dict[model] = dict(eval(ori_mb))
        size_num_raw = size[:-1]
        if '.' in size_num_raw:
            size_num = float(size_num_raw)
        else:
            size_num = int(size_num_raw)
        size_uni = size[-1]
        model_dict[model][size_uni].append(size_num)
    sorted_dict = sorted(model_dict.items())

    def print_dict(name, sizes):
        result = f"{name}: "
        m_sizes = sorted(sizes['M'])
        for size in m_sizes:
            result += f'{size}M, '
        b_sizes = sorted(sizes['B'])
        for size in b_sizes:
            result += f'{size}B, '
        print(result[:-2])

    for pair in sorted_dict:
        print_dict(pair[0], pair[1])


def q5_body(qualities, prices):
    def find_median(nums):
        sorted_nums = sorted(nums)
        if len(nums) % 2 == 0:
            max_middle = len(nums) // 2
            return (sorted_nums[max_middle] + sorted_nums[max_middle - 1]) / 2
        else:
            return sorted_nums[len(nums) // 2]

    median_quality = find_median(qualities)
    median_price = find_median(prices)
    result = 0
    for _ in range(len(qualities)):
        if qualities[_] > median_quality and prices[_] < median_price:
            result += 1
    print(result)


def q5():
    n = int(input())
    qualities = []
    distances = input().strip().split()
    prices = list(map(int, input().split()))
    for i in range(n):
        distance = distances[i]
        x, y = tuple(eval(distance))
        qualities.append((x + y) / prices[i])
    q5_body(qualities, prices)


q5()