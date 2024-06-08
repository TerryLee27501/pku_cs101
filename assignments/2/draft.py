import math


def is_prime(n):
    if n == 1: return False
    if n == 2 or n == 3: return True
    range_max = int(math.sqrt(n))
    for i in range(2, range_max+1):
        if n % i == 0:
            return False
    return True


def is_square(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False


def is_T_prime(n):
    if n % 2 == 0 and n != 4:
        return 'NO'
    if is_square(n):
        if is_prime(math.sqrt(n)):
            return 'YES'
    return 'NO'


ignored = input()
nums = map(int, input().split())
for num in nums:
    print(is_T_prime(num))