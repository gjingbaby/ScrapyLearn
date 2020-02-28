# Pandas使用

### 1.Tushare获取财经数据

~~~ python
import tushare as ts
import pandas as pd
#设置自己的token，需要在tushare注册获取，相当于key
# ts.set_token("0b32a25ad92f09bcf7bb160c7b203033781f9b23db7ba4d1917bb436")
# #初始化接口
# pro = ts.pro_api()
# 获取每日数据，参数为证券代码，返回的数据从历史到获取时间为止，一天一行
df_000001 = pro.daily(ts_code = "000001.SZ")
df_000002 = pro.daily(ts_code = "000002.SZ")
~~~

**注意事项**

1. Tushare返回的数据是pandas格式的数据
2. Tushare依赖库包括pandas和lxml

### 2.pandas存储数据

~~~python
# 实例化一个pandas的writer
writer = pd.ExcelWriter(r"E:\pyworkspace\RawData.xlsx")
df_000001.to_excel(writer,"sheet1")
df_000002.to_excel(writer,"sheet2")
writer.save()
~~~

**注意事项**

1. 使用pandas向excel写入数据，比xlwings简洁
2. 通过实例化一个excel的写入类ExcelWriter，向excel写入数据
3. 再使用tushare的to_excel函数写入具体表格

### 3.通过win32com.client获取互动表格指定内容

~~~python
import win32com.client as win32
import pandas
#获取表格内容
OurExcelApp = win32.GetActiveObject("Excel.Application")
# RangeSelect = OurExcelApp.Range("A1:L5001").Value
RangeSelect = OurExcelApp.Sheets("sheet2").Range("A1:L5001").Value
# RangeSelect = OurExcelApp.Workbooks("RawData.xlsx").Sheets("sheet2").Range("A1:L5001").Value
# print(RangeSelect)
# print(type(RangeSelect))
~~~

**注意事项**

- win32获取的激活的excel对象（进程）可以包括多个，在存在多个进程的时候，为了获取指定的excel必须使用Workbooks("工作簿1")指定具体工作簿，当一个工作簿中包含多个sheet时，使用Sheets("sheet2")指定具体工作表；当只有一个工作簿时，可以直接获取单元格值，此处工作簿为当前工作簿，工作表为第一个默认sheet1。

### 4.获取的指定excel内容导入pandas

```python
#导入pandas，生成DataFrame格式数据
#先生成Series格式，再转成dataframe
Raw_Series_Data = pd.Series(RangeSelect)
#标题
Column_Data = Raw_Series_Data[0]
#数据
Trade_Data = Raw_Series_Data[1:]
#使用pd.DataFrame
Ready_Data_Frame = pd.DataFrame(data=list(Trade_Data),columns=Column_Data)
# print(Ready_Data_Frame.head())

```

### 5.使用pandas整理数据sklearn回归分析

~~~ python
#再pandas中进行回归分析
#导入线性模型中的线性回归分析函数
from sklearn.linear_model import LinearRegression
#导入可视化工具
import matplotlib.pyplot as plt
#选取回归分析涉及的xy数据
#iloc是pandas的查找函数
X = Ready_Data_Frame.iloc[:,6].values.reshape(-1,1)
# print(X)
Y = Ready_Data_Frame.iloc[:,10].values.reshape(-1,1)
# print(Y)
#回归分析
LR_Model = LinearRegression()
LR_Model.fit(X,Y)
Y_Predict = LR_Model.predict(X)
~~~

### 6.使用matplotlib可视化

~~~python
#可视化
plt.scatter(X,Y,color='blue')
plt.plot(X,Y_Predict,color='red')
plt.show()
~~~

