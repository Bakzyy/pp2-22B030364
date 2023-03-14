# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

import math

def custom_gen(max):
    n = 1
    while n <= max:
        if n % 12 == 0:
            yield n
        n += 1

n = int(input())

for i in custom_gen(n):
    
    print(i)