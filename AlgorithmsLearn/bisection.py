
'''
本包内代码根据https://github.com/TheAlgorithms/Python而来，
旨在学习python中的算法实现
怎么有效，简洁的实现算法
'''


'''代码解释

二分法（Bisection method） 即一分为二的方法. 设[a，b]为R的闭区间. 
逐次二分法就是造出如下的区间序列([an，bn])：a0=a，b0=b，
且对任一自然数n，[an+1，bn+1]或者等于[an，cn]，或者等于[cn，bn]，其中cn表示[an，bn]的中点.

给定精确度ξ,用二分法求函数f(x)零点近似值的步骤如下:
1 确定区间[a,b],验证f(a)·f(b)<0,给定精确度ξ.
2 求区间(a,b)的中点c.
3 计算f(c).

(1) 若f(c)=0,则c就是函数的零点;
(2) 若f(a)·f(c)<0,则令b=c;
(3) 若f(c)·f(b)<0,则令a=c.
(4) 判断是否达到精确度ξ:即若|a-b|<ξ,则得到零点近似值a(或b),否则重复2-4'''

import math
def bisection(function,a,b):

    start = a
    end = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif function(a)*function(b) > 0:
        print("could not find root in [a,b]")
        return
    else:
        mid = start + (start-end)/2.0
        while abs(start-mid) > 10**-7:
            if function(mid) == 0:
                return mid
            elif function(start)*function(mid) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end-start)/2.0
        return mid


def f(x):
    return math.pow(x,2)-2*x-5

if __name__ == "__main__":
    print(bisection(f,1,108))
