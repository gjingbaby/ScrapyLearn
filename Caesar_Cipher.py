
'''加密解密程序
encrypt 加密
decrypte 解密
加密方法是凯撒的偏移加密法，加密核心是偏移（shift）的字母个数,利用ord(),chr()函数，主要基于ASCII码
以下代码中偏移量受限制，未能解决偏移量过大造成的加密解密问题
'''

def encrypt(enText,enShift):
    encrypt_Text = enText
    shift_number = enShift
    encrypt_result = ""
    # isalpha()方法检测字符串是否只由字母组成。
    for i in encrypt_Text:
        #进行偏移
        After_convert = ord(i) + shift_number
        if i.isalpha():
            if After_convert > ord("z"):
                After_convert -= 26
            elif After_convert > ord("Z") and After_convert < ord("a"):
                After_convert -= 26
        elif i.isdigit():
            if After_convert > ord("9"):
                After_convert -= 9
        #print(i,After_convert,chr(After_convert))
        encrypt_result = encrypt_result + chr(After_convert)

    print(encrypt_result)

def decrypye(deText,deShift):
    decrypte_Text = deText
    shift_number = deShift
    decrypte_result = ""
    # isalpha()方法检测字符串是否只由字母组成。
    for i in decrypte_Text:
        After_convert = ord(i) - shift_number
        if i.isalpha():
            if After_convert > ord("Z") and After_convert < ord("a") or After_convert < ord("A"):
                After_convert += 26
        elif i.isdigit():
            if After_convert < ord("0"):
                After_convert += 9
        #print(i, After_convert, chr(After_convert))
        decrypte_result = decrypte_result + chr(After_convert)
    print("解密信息完成：",decrypte_result)


if __name__ == "__main__":
    enText = input("请输入要加密的文本：")
    enShift = int(input("请输入加密偏移量(1-26)："))
    encrypt(enText,enShift)
    deText = input("请输入要解密的文本：")
    deShift = int(input("请输入解密偏移量："))
    decrypye(deText,deShift)







