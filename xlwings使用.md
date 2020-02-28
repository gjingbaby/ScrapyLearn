# xlwings使用

## 1.创建新表格

```python
import xlwings as xw
wb = xw.Book()
wb.sheets["sheet1"].range("A1").value = "编号"
wb.save()
wb.close()
```

**注意事项**

1）直接创建workbook的instance

2）使用顺序workbook---->sheet---->range

3）赋值符合vba的习惯

## 2.连接已有表格

```python
#打开已有表格时，表格文件路径最好手写，从其他地方粘贴的地址可能包含其他字符，导致找不到文件
wb = xw.Book(r"c:\users\administrator\desktop\hello.xlsx")

app1 = xw.App(visible=True,add_book=False)
wb1 = app1.books.open(r"c:\users\administrator\desktop\hello.xlsx")
```

**注意事项**

1）从文件/安全处复制的文件路径，因为从左到右复制的手法，会使复制文件中包含多余字符（u202A），导致文件路径再程序中读取时不正确/找不到。

2）以上时两种连接现有表格的方法，上边一种为最新方法。、

## 3.读取表格内容

```
import xlwings as xw
wb = xw.Book(r"c:\users\administrator\desktop\hello.xlsx")
a = wb.sheets["sheet1"].range("A1:D2")
#range是一个可迭代的对象
for cell in a:
    if cell.value == None:
        cell.value = "hello"
    print(cell.value)
wb.save()
wb.close()
```

**注意事项:读取到的range是一个可迭代对象**

## 4.区域赋值

```python
import xlwings as xw
import time

wb = xw.Book()
head_row = ["姓名","部门","分数"]
first_row = ["林芝","规划部","87"]
sht = wb.sheets["sheet1"]
#限定区域,列表填入
sht.range("A1:C1").value = head_row
sht.range("A2:C2").value = first_row
#锚定起点，根据数据扩展
sht.range("A3").value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
#使用pandas
import pandas as pd
df = pd.DataFrame([[1,2],[3,4]],columns=["a",'b'])
sht.range("A5").value = df

for i in range(10,21):
    sht.range("A%d"%i).value = i

wb.save(r"c:\users\administrator\desktop\world.xlsx")
time.sleep(10)
wb.close()
```

**注意事项**

1）可对指定区域（单行），使用列表赋值

2）对列进行赋值时，不可直接使用列表赋值，**可使用转置函数**

```python
wb = xw.Book()
sht = wb.sheets["sheet1"]

headline = ["名称","编号"]
sht.range("A1:B1").value = headline
#sample函数从特定列表范围内选取不重复的指定个数的数字
column_mc = random.sample(range(1,100000),10000)
column_bh = random.sample(range(1,50000),10000)
#从锚点开始赋值，使用转置
sht.range("A2").options(transpose=True).value = column_mc
sht.range("B2").options(transpose=True).value = column_bh

wb.save(r"c:\users\administrator\desktop\world.xlsx")
time.sleep(10)
wb.close()
```

3）矩阵数据/list数据可根据**锚点**输入表格