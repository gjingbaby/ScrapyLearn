'''
import math
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

#杨辉三角
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


#返回函数

def _sum(*args):
    a = 0
    for i in args:
        a = a + i
    return a

a = _sum(1,2,3,4,5)
print(a)

def lazy_sum(*args):
    def _sum():
        a = 0
        for i in args:
            a = a + i
        return a
    return _sum
b = lazy_sum(3,4,5,6)
print(b)

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()   #f1,f2,f3组成列表
print(f1(),f2(),f3())  #此处结果为9，9，9；因为fs存储的是函数，当第三次返回时i = 3，所以最后调用时都以3为准

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))   #此处直接将i赋值给f函数，固定了其参数，同时也得益于代码结构的分开
    return fs

f1,f2,f3 = count()   #此处的赋值结果是f1,f2,f3是三个未被调用的函数
print(f1(),f2(),f3())


#匿名函数

a = list(map(lambda x:x*x,[x for x in range(1,10)]))
print(a)

b = list(filter(lambda n : n % 2 == 1,range(1,20)))
print(b)



#装饰器
import functools
def log(func):
    @functools.wraps(func)     #把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    def wrapper(*args,**kwargs):
        print('call %s:'%func.__name__)
        return func(*args,**kwargs)
    return wrapper

@log
def now():
    print('hello')
now()



def log(text):
    def decorator(func):
        @functools.wraps(func)   #把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
        def wrapper(*args,**kwargs):
            print(text,func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('excute:')
def now():
    print('hello world')

now()   #函数执行时相当于 log('excute:')(now)

import time
def logTime(func):

    def wrapper(*args,**kwargs):
        print('开始时间：',time.ctime())
        return func(*args,**kwargs)
    return wrapper


@logTime
def timeclock():
    print('hello world')

for i in range(10):
    timeclock()
    time.sleep(5)



#class and instance

class student():
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def gtName(self):
        return self.__name
    def gtScore(self):
        return self.__score
    def stScrore(self,newscore):
        if newscore < 100 and newscore > 0:
            self.__score = newscore
        else:
            raise ValueError('Please Input Right Score.')
    def prtscore(self):
        print('The score of %s is %d.'%(self.__name,self.__score))

    def gtlevel(self):
        if self.__score > 90:
            return 'The level of %s is A'%(self.__name)
        elif self.__score < 60:
            return 'The level of %s is C'%(self.__name)
        else:
            return 'The level of %s is B'%(self.__name)

stdt1 = student('jack',76)
print(stdt1.gtName())
print(stdt1.gtScore())
print(stdt1.gtlevel())
stdt1.stScrore(80)
print(stdt1.gtScore())
print(stdt1._student__name)



#继承和多态和鸭子类型

class Animal():
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
class Cob(Animal):
    def run(self):
        print('Cob is running...')


def run_twice(anim):
    anim.run()
    anim.run()

dog = Dog()
run_twice(dog)

cat = Cat()
run_twice(cat)

cob = Cob()
run_twice(cob)

print(isinstance(dog,Dog))
print(isinstance(cat,(Cat,Animal)))
print(dir(dog))
a = 'abc'
print(dir(a))

class student():
    count = 0
    def __init__(self,name):
        self.name = name
        student.count += 1

s1 = student('jack')
s2 = student('mary')
s3 = student('lucy')
print(student.count)



class author():
    pass

#给实例绑定任意属性
a1 = author()
a1.name = 'jack'
print(dir(a1))

#给实例绑定方法
from types import MethodType

def set_score(self,score):
    self.score = score

a4 = author()
a4.set_score = MethodType(set_score,a4)
a4.set_score(90)
print(a4.score)


#给类绑定任意属性
author.name = 'mary'
a2 = author()
print(a2.name)

#给类绑定方法
def gtName(self,name):
    self.name = name
author.gtName = gtName
a3 = author()
a3.gtName('cuidis')
print(a3.name)

#使用 __splots__限制类添加的属性

class human():
    __slots__ = ('name','age')


h1 = human()
h1.name = 'linch'
print(h1.name)

h1.score = 90
print(h1.score)


#关于property装饰器使用
class student():
    pass
s1 = student()
s1.score = 90

# 此处给实例绑定任意属性,存在问题：
# 1、无法对绑定的属性的值进行检查，数据无效的风险
# 2、那么采用第二种方式，在类里边中定义方法，进行检查

class teacher(object):
    def stScore(self,score):
        if 0 <= score <= 100:
            self.score = score
        else:
            print('Input Right Score!')
            self.score = 'WRONG SCORE'
    def gtScore(self):
        return self.score
t1 = teacher()
t1.stScore(120)
print(t1.gtScore())

# 1、在类中定义方法，对score属性进行检查，实现了控制风险的目的。
# 2、但是稍显麻烦，不简洁
# 3、使用@property装饰器

class commander(object):

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self,value):
        if 0 <= value <= 100:
            self.score = value
        else:
            print('Input Right Score!')
            self.score = 'WRONG SCORE'
c1 = commander()
c1.score = 60
print(c1.score)

#此处可以把函数像属性一样赋值，并检查
#还是暂时不用@property，直接给类加属性
#此处有递归最大变量的问题未解决

#多重继承

class AnimalMixIn(object):
    def miemie(self):
        print('I am an animal.')

class RunableMixIn(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(AnimalMixIn,RunableMixIn):
    pass

d1 = Dog()
d1.run()
d1.miemie()

#定制类

class student(object):

    def __init__(self,name):
        self.name = name
    #设置实例print出来的效果
    def __str__(self):
        return  'student object(name:%s)'%self.name
    #设置实例直接敲出来，不用print的效果
    __repr__ = __str__   #两个内容一样，赋值过去
s1 = student('jack')
print(s1)


class Fib(object):          #给类增加迭代属性，使类可迭代
    def __init__(self,mx):
        self.a,self.b = 0,1
        self.mx = mx
    #可迭代函数和next方法
    def __iter__(self):
        return self
    def __next__(self):
        self.a ,self.b = self.b,self.a + self.b
        if self.a > self.mx:
            raise StopIteration
        return self.a

    # 虽然有了可迭代，但是不能像list一样，读取数据
    def __getitem__(self,n):
        if isinstance(n,int):     #n是整数的时候
            a,b = 1,1
            for i in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice):    #n是切片的时候
            start  = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            l1 = []
            for i in range(stop):
                if i >= start:
                    l1.append(a)
                a,b = b,a+b
            return l1
f1 = Fib(1000)
for i in f1:
    print(i)
print('It is',f1[10])
print('It is',f1[10:15])

class student(object):
    def __init__(self,name):
        self.name = name
    def __getattr__(self, item):
        if item == 'score':
            return 98

s1 = student('mary')
print(s1.name)
print(s1.score)
print(s1.year)


class Chain(object):
    def __init__(self,path = ''):
        self.path = path
    def __getattr__(self, item):
        return Chain('%s/%s'%(self.path,item))
    def __str__(self):
        return self.path

c1 = Chain('hello').store.user.name.line
print(c1)



class student(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):   #调用实例本身
        return 'My Name Is %s'%self.name

s1 = student('lucy')
print(s1())               #调用实例本身


def foos(s):
    n = int(s)
    assert n != 0,'n is zero'   #意思是n != 0这个表达式应该是True，否则肯定会报错
    return 10/n
def main():
    foos('0')

main()    #报错： AssertionError: n is zero  


with open('规划法规体系.md','r',encoding='UTF-8') as f:
    ctt = f.read()   #读取全部内容
    print(ctt)

with open('规划法规体系.md','r',encoding='UTF-8') as f:
    for i in range(10):
        ctt = f.readline()   #每次读取一行
        print(ctt)


with open('规划法规体系.md','r',encoding='UTF-8') as f:
    ctt2 = f.readlines()  #一次读取所有内容并按行返回
    for i in range(len(ctt2)):
        print('第%d行'%(i+1)+ctt2[i])


with open(r'D:\pyworkspace\ScrapyLearn\AlgorithmsLearn\blur.jpg','rb') as p:
    ctt = p.read()
    with open('blur1.jpg','wb') as p1:
        p1.write(ctt)

from io import StringIO
#向内存中写入str
f = StringIO()
ctt = f.write('hello')
ctt1 = f.write(' ')
ctt2 = f.write('world!')
print(f)
print(f.getvalue())
#读取内存中str
f = StringIO('hello\nhi\ngoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#写入，读取bytes内容
from io import BytesIO
f = BytesIO()
ctt = f.write('中国 '.encode('utf-8'))
print(ctt)
print(f.getvalue())


import os

#print(os.name)
print(type(os.environ))
paths = os.environ.get('path')
paths_list = paths.split(';')
for i in paths_list:
    print(i)


import os
import sys
import time

pth3 = os.path.abspath('..')
pth1 = os.getcwd()
os.chdir(r'c:\python37')
pth = os.path.abspath('.')
pth2 = sys.argv[0]
print(pth)
print(pth3)
print(pth1)
print(pth2)

ndirpth = os.path.join(pth,'testdir')
ndirpth1 = os.path.split(pth2)
ndirpth2 = os.path.splitext(pth2)

print(ndirpth)
print(ndirpth1)
print(ndirpth2)

os.mkdir(ndirpth)

time.sleep(5)
if os.path.isdir(ndirpth):
    os.rmdir(ndirpth)


import os 
dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
for i in dirs:
    print(i)

dirs1 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

for i in dirs1:
    print(i)

#序列化    使用dumps函数 
import pickle
d = dict(name = 'bob',age = 20,score = 88)
d_pk = pickle.dumps(d)
with open('PickleData.txt','wb') as f:
    f.write(d_pk)
    print(d_pk)

#反序列化   使用load函数
import pickle
f1 = open('PickleData.txt','rb')
d1 = pickle.load(f1) 
f1.close() 
print(d1)
print(type(d1))

#序列化为json数据
#json数据是字符串，各种语言都能读取
import json
#将dict序列化成json数据，使用dumps函数
d = dict(name = 'bob',age = 20,score = 88)
d_dumps_byjson = json.dumps(d)
print(d_dumps_byjson)
print(type(d_dumps_byjson))
#将json数据反序列化成dict，使用loads函数
d_load_byjson = json.loads(d_dumps_byjson)
print(d_load_byjson)
print(type(d_load_byjson))


#class对象的json序列化和反序列化
import json

class student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s1 = student('jack',23,90)

def studentTojson(ins):
    return {'name':ins.name,'age':ins.age,'score':ins.score}
#使用转换函数，将实例转换成dict，再dumps进行json序列化
s1_dumps_byjson = json.dumps(s1,default=studentTojson)
print(s1_dumps_byjson)
#调用实例的字典私有属性，转换成dict，再进行json序列化
s1_dumps_byjson = json.dumps(s1,default=lambda obj: obj.__dict__)
print(s1_dumps_byjson)

#反序列化
#将json数据转换成实例的函数
def dictToinstance(dic):
    return student(dic["name"],dic["age"],dic["score"])
#反序列化时定义object_hook=,将dict转换成实例
s1_loads_byjson = json.loads(s1_dumps_byjson,object_hook=dictToinstance)
print(s1_loads_byjson,type(s1_loads_byjson))



#import threading
import multiprocessing
import os

def run_proc(name):
    print("Run child process %s (%s)"%(name,os.getpid()))

if __name__ == "__main__":
    print("Parent process %s"%os.getpid())
    p = multiprocessing.Process(target=run_proc,args=('test',))
    print('Child process start')
    p.start()
    p.join()
    print('child process end')


'''
import multiprocessing
import os,time,random

def long_time_task(name):
    print('run task %s (%s)'%(name,os.getpid()))
    stt = time.time()
    time.sleep(random.random()*3)
    nd = time.time()
    print('task %s run %0.2f'%(name,(nd-sdt))

if __name__ == '__main__':

    print('Parent process %s'%os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for all subprocess done...')
    p.close()
    p.join()
    print('all subprocess done.')








