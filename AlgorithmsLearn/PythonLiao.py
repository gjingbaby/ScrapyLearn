

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
li = [x for x in range(1,100) if x%2 == 1]
#list区别在于（）保存的是算法
gene = (x for x in range(1,100) if x%2 == 0)
for i in range(10):
    print(next(gene))
for i in gene:
    print(i)

#斐波那契数列
def fib(max):
    n,a,b = 0,0,1
    while max > n:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'Done'

#将以上函数转变成generator
def fib(max):
    n,a,b = 0,0,1
    while max > n:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'Done'
a = fib(5)
print(a)
'''

#杨辉三角
'''
第一行  [1,2,1]
第二行计算方式  0,1,2,1
              +1,2,1,0
              =1,3,3,1
              可以看出是在给第一行的list前后补零相加而成的

def triangeles(n):
    b = [1]
    while len(b) < n:
        print(b)
        c = [0]+b
        d = b+[0]
        b = [c[i]+d[i] for i in range(len(c))]
triangeles(10)

def triangels():
    b = [1]
    while True:
        yield b
        #此处为什么不直接写成B.insert(0,0),原因在于insert函数直接修改原列表，并没有返回值，所以c会返回None
        c = [0] + b
        d = b + [0]
        b = [c[i]+d[i] for i in range(len(c))]
n = 1
for i in triangels():
    n = n + 1
    print(i)
    if n > 10:
        break
        
        

def nature(m):
    n = 0
    while n < m:
        yield n
        n += 1
h = nature(1000)
print(h)
for i in nature(1000):
    print(i)

#高阶函数

def highorderFunction(fun,a,b):
    return fun(a),fun(b)
c = highorderFunction(abs,-10,2)
print(c)

def fun(x):
	return x*x
li = [x for x in range(10)]
new_li = map(fun,li)
print(type(new_li))

from functools import reduce
def addnum(x,y):
    return x*10+y
li = [x for x in range(1,20,2)]
r = reduce(addnum,li)
print(r)

def usersipt(n):
    users = []
    for i in range(n):
        ipt = input('Please Input Some Words:')
        users.append(ipt)
    return users
def firstNum(str):
    return str[0].upper()+str[1:]
li = list(map(firstNum,usersipt(5)))
print(li)

'''
# 生成所有的质数，使用生成器

def _odd_iter():    #基数生成器
    n=1
    while True:
        n = n + 2
        yield n

def _not_divisiable(n):    #筛选函数
    return lambda x : x % n > 0    #此处表示余数大于0，即反向筛选出余数是0的，即可以整除的奇数

def primes():
    yield 2
    it = _odd_iter()  #初始化序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n),it)  #筛选序列
'''
m = 1
for i in primes():
    print(i)
    m = m + 1
    if m > 50:
        break

for i in primes():
    if i < 1000:
        print(i)
    else:
        break

str = 'gjingbabylinchyeats'
print(str[1:5])
print(str[:5])
print(str[1:])
print(str[::5])  #从头开始每隔5个字符取一个
print(str[1::5])  #从第二位开始每隔5个字符取一个
print(str[::-1])  #从0开始每隔-1取一个，就是逆序
print(str[-1::-1])  #同上



def natureNum():    #自然数生成器
    n = 1
    while True:
        yield n
        n = n + 1

def _intTostr(m):   #筛选逆序后与原来相同的数字
    if str(m) == str(m)[::-1]:
        return m

def huishu():    #使用filter筛选，此处直接使用函数名_intTostr，因只有一个参数，即由后边生成器提供
    return filter(_intTostr,natureNum())   #若有多个参数，正常就会继续引入参数_intTostr(n)，n需要定义
#返回的filter为迭代器
for i in huishu():
    if i < 1000:
        print(i)
    else:
        break

'''
li = [-33,-4,23,90,-6]          #数字列表
lis = sorted(li)                #无参数按大小排序
li_sort = sorted(li,key=abs)    #按绝对值大小排序
strli = ['Gjingbaby','yeats','Linch','baby']
s1 = sorted(strli)              #按ascii字母顺序
s2 = sorted(strli,key=str.lower)  #按首字母小写排列
s3 = sorted(strli,key=str.lower,reverse=True)   #按首字母小写排列后，再逆序
print(s2,'\n',s3)
a= 'linchyeats'
b = reversed(a)
c = [i for i in b]
print(''.join(c))