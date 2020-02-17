'''
获取范围内的质数
'''

primes = [2]
for number in range(2,100):
    for prime in primes:
        result = number % prime
        if result is 0:
            break
        sqrt = number ** 0.5    #number的平方根是sqrt
        if sqrt < prime:
            primes.append(number)
            break
print(primes)
