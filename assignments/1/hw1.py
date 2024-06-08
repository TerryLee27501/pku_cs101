def tbnc(n):
    if n == 1 or n == 2: return 1
    else:
        tbnc_list = [0, 1, 1]
        while n >= len(tbnc_list):
            tbnc_list.append(tbnc_list[-3] + tbnc_list[-1] + tbnc_list[-2])
        return tbnc_list[n]



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


#k = input()
#print(f'n^{mono_compare(poly_split(k))}')


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

'''
count_list = [0]
    for _ in range(100):
        count_list.append(0)
    for vote in votes_list:
        vote = int(vote)
        count_list[vote] += 1
    options, max_number = '', 0
    for option, number in enumerate(count_list):
        if number > max_number:
            max_number = number
            options = str(option)
        elif number == max_number:
            options += ' ' + str(option)'''