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

'''
num_list = input().split()
first_fraction = Fraction(int(num_list[0]), int(num_list[1]))
second_fraction = Fraction(int(num_list[2]), int(num_list[3]))
first_fraction.to_add(second_fraction)
print(first_fraction)
'''


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
        if max_weight >= total_weight:
            if max_weight >= total_weight + candy[2]:
                total_value += candy[1]
                total_weight += candy[2]
            else:
                total_value += candy[0] * (max_weight - total_weight)
                break
        else: break
    return total_value


print("{:.1f}".format(value_calculator(*q2_parser())))

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


#votes_count(input())
