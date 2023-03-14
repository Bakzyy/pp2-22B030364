# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

import math

def even_gen(max):
    n = 1
    while n <= max:
        if n % 2 == 0:
            yield f"{n}, "
        n += 1

n = int(input())
res = ""

for i in even_gen(n):
    res += i

print(res)