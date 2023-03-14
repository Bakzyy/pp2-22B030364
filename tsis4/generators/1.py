# Create a generator that generates the squares of numbers up to some number N.

import math

def square_gen(max):
    n = 1
    while n <= max:
        yield n ** 2
        n += 1


n = int(input())

for i in square_gen(n):
    
    print(i)
    