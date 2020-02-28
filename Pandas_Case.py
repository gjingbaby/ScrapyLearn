import tushare as ts
import pandas as pd
#设置自己的token，需要在tushare注册获取，相当于key
# ts.set_token("0b32a25ad92f09bcf7bb160c7b203033781f9b23db7ba4d1917bb436")
# #初始化接口
# pro = ts.pro_api()
# #获取每日数据
# df_000001 = pro.daily(ts_code = "000001.SZ")
# df_000002 = pro.daily(ts_code = "000002.SZ")
# #实例化一个pandas的writer
# writer = pd.ExcelWriter(r"E:\pyworkspace\RawData.xlsx")
# df_000001.to_excel(writer,"sheet1")
# df_000002.to_excel(writer,"sheet2")
# writer.save()

import win32com.client as win32
import pandas
#获取表格内容
OurExcelApp = win32.GetActiveObject("Excel.Application")
# RangeSelect = OurExcelApp.Range("A1:L5001").Value
RangeSelect = OurExcelApp.Sheets("sheet2").Range("A1:L5001").Value
# RangeSelect = OurExcelApp.Workbooks("RawData.xlsx").Sheets("sheet2").Range("A1:L5001").Value
# print(RangeSelect)
# print(type(RangeSelect))

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
#可视化
plt.scatter(X,Y,color='blue')
plt.plot(X,Y_Predict,color='red')
plt.show()
