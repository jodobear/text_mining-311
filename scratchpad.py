u = set()
a = [1, 2, 3, 1]
u |= a
print(u)

import random

sh_path = dict()
def find_sh_path(G, s=list(G)[random.randrange(1000)], t=list(G)[random.randrange(1000)]):
    return s, t, nx.shortest_path(G, source=s, target=t, method='dijkstra')

i = 1000
while i > 0:
    s, t, path = find_sh_path(G)
    sh_path[(s, t)] = path
    i -= 1




def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

print([fib(n) for n in range(-1)])

def is_prime(n):
    import math
    if n < 2:
        return False  # 0 & 1 are not
    if n < 4:
        return True  # 2 & 3 are
    if n % 2 == 0:
        return False # evens
    odds = range(3, int(math.sqrt(n)) + 1, 2)
    return not any(n % i == 0 for i in odds)

print(is_prime(7))

def palindrome(string):
    rev = string[::-1]
    return rev == string

print(palindrome("aaa"))
print(palindrome("aba"))
print(palindrome("aac"))

import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(np.argsort(a[::-1])[:3])