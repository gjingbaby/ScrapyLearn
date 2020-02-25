import xlwings as xw
import random
import time
# excel_list = []
# for i in range(10):
#     # 先创建instance，add_book = False时，excel不显示
#     excel_list.append(xw.App(visible=True,add_book=True))
#     print("openning  "+ str(i+1))
#
# for i in range(10):
#     print("closing   "+str(i+1))
#     #关闭打开的instance，实际是windows的进程
#     excel_list[i].quit()

# wb = xw.Book()
# wb.sheets["sheet1"].range("A1").value = "编号"
# wb.save()

# app1 = xw.App(visible=True,add_book=False)
# wb1 = app1.books.open(r"c:\users\administrator\desktop\hello.xlsx")


#打开已有表格时，表格文件路径最好手写，从其他地方粘贴的地址可能包含其他字符，导致找不到文件
# wb = xw.Book(r"c:\users\administrator\desktop\hello.xlsx")
# a = wb.sheets["sheet1"].range("A1:D2")
# #range是一个可迭代的对象
# for cell in a:
#     if cell.value == None:
#         cell.value = "hello"
#     print(cell.value)
# wb.save()
# wb.close()

# wb = xw.Book()
# head_row = ["姓名","部门","分数"]
# first_row = ["林芝","规划部","87"]
# sht = wb.sheets["sheet1"]
# #限定区域。列表填入
# sht.range("D1:D3").value = head_row
# sht.range("A2:C2").value = first_row
# #锚定起点，根据数据扩展
# sht.range("A3").value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
# #使用pandas
# import pandas as pd
# df = pd.DataFrame([[1,2],[3,4]],columns=["a",'b'])
# sht.range("A5").value = df
# #使用迭代，将列表放入column
# for i in range(10,21):
#     sht.range("A%d"%i).value = i

#使用转置将数据填入column


wb = xw.Book()
sht = wb.sheets["sheet1"]

headline = ["名称","编号"]
sht.range("A1:B1").value = headline

column_mc = random.sample(range(1,100000),10000)
column_bh = random.sample(range(1,50000),10000)
sht.range("A2").options(transpose=True).value = column_mc
sht.range("B2").options(transpose=True).value = column_bh

wb.save(r"c:\users\administrator\desktop\world.xlsx")
time.sleep(10)
wb.close()



