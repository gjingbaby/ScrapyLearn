'''
从题库里随机抽取题号，题库中有单选，多选，判断
利用Python中的random.sample()函数实现
range()函数返回的是一个可迭代对象而不是列表，需要列表的话使用list（）转换
使用sorted()排序
'''

import random
DanXuan = random.sample(range(1,98),40)
DuoXuan = random.sample(range(99,115),10)
print(sorted(DanXuan))
print(sorted(DuoXuan))
