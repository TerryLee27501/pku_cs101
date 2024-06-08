import math

def sieve(n):
    sieve_list = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n))):
        if sieve_list[i]:
            for j in range(i*i, n+1, i):
                sieve_list[j] = False
    return sieve_list


def is_T_prime(i):
    if i < 4:
        return False
    if math.sqrt(i) == int(math.sqrt(i)) and sieve_list[int(math.sqrt(i))]:
        return True
    return False


def average_calculate(scores):
    total = 0
    for score in scores:
        if is_T_prime(score):
            total += score
    if total == 0: return 0
    return "{:.2f}".format(total / len(scores))


sieve_list = sieve(10000)
students_num = int(input().split()[0])
for _ in range(students_num):
    scores = list(map(int, input().split()))
    print(average_calculate(scores))