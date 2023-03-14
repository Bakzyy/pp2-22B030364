# Implement a generator that returns all numbers from (n) down to 0.

import math

def rev_gen(start):
    n = start
    
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for i in rev_gen(n):
    
    print(i)