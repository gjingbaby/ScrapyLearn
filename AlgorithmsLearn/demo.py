

import math
'''
def quadratic(a,b,c):
    if b*b > 4*a*c:
        x = (-b + math.sqrt(b*b-4*a*c))/2*a
        y = (-b - math.sqrt(b*b-4*a*c))/2*a
        print(x,y)
    else:
        print('No solution')

quadratic(1,3,-4)


def chengji(*args):
    s = 1
    for i in args:
        s = s * i
    print(s)

chengji(1,2,3,5,6)


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
    
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

n = fact_iter(100,1)
print(n)

'''

a = list(range(1,100))
print(a[2:10])
print(a[-9:-1])
print(a[:10])

def MaxMin(li):
    maxValue = max(li)
    minValue = min(li)
    return maxValue,minValue
def MinMax(li):
    maxValue = li[0]
    minValue = li[0]
    for i in li[1:]:
        if i > maxValue:
            maxValue = i
        if i < minValue:
            minValue = i
    return maxValue,minValue
import random
a = random.sample(range(1,100),5)
print(a)
b = MinMax(a)
print(b)


#生成器

