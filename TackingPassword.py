'''破解密码
1.破解的前提是已经指导是使用的加密算法，以下程序是针对凯撒加密后的明文进行破解
2.以下程序是对偏移量从小到大的一个测试，根据不同的偏移量，得出不同的结果
3.得出的结果需要人工判读
4.添加断点之后，可以运行debug模式，检查代码运行
'''


def hackingPwd(message,Letters):
    for key in range(len(Letters)):
        translited = ""
        for symbol in message:
            if symbol in Letters:
                num = Letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num +len(Letters)
                translited = translited + Letters[num]
            #else表示没有进行加密的str
            else:
                translited = translited + symbol
        print("破解key是%s，破解结果是%s"%(key,translited))

if __name__ == "__main__":
    message = "lonslgfgd"
    Letters = "abcdefghijklmnopqrstuvwxyz"
    hackingPwd(message,Letters)




