# python中使用win32com接口

### 1、pywin32

- pywin32封装了几乎所有的WindowsApi接口，可以通过python方便调用Windows的功能
- pywin32同步安装了win32com，可以通过python进行COM编程
- python第三方库安装目录下，win32文件夹下是所有WindowsApi支撑模块，win32com文件夹下是COM的支撑模块

### 2、监听事件

~~~ python
import win32com.client as win32
#client是客户端的意思，常见的cs结构，即client/server.
import pythoncom

#给应用内定义事件，事件在此处由定义的函数实现，定义的函数是由windows定义的，因此函数名称不能错
class AapplicationEvents:
    def OnSheetActivate(self,*args):
        print("该工作表被选中了")
class WorkBookEvents:
    def OnSheetSelectionChange(self,*args):
        print(args[1].Address)
#获取激活的excel应用对象
excel1 = win32.GetActiveObject("Excel.Application")
#监听选中sheet的事件，sheet被选中后，输出写好的print内容
excel1_events = win32.WithEvents(excel1,AapplicationEvents)
#获取指定的excel，Workbooks方法是特有名词，不能拼写错误
excel2 = excel1.Workbooks("工作簿1")
#监听工作簿1内选择cell的事件，输出选取的cell地址
excel2_events = win32.WithEvents(excel2,WorkBookEvents)


while True:
    #使用pythoncom弹出消息
    pythoncom.PumpWaitingMessages()
~~~

**注意事项**

1. 首先获取激活应用对象，其次给对象编写事件，最后对激活对象的特定事件进行监听。

2. 在编写对象事件时，应注意函数名称的规范性，这些名称已在windows中定义过，此处只是前缀On。

3. 编写对象事件时的主要事件可以在[VbaForOffice](https://docs.microsoft.com/zh-cn/office/vba/api/excel.application.sheetactivate)的文档中查阅。

4. win32获取的激活的excel对象（进程）可以包括多个，在存在多个进程的时候，为了获取指定的excel必须使用Workbooks("工作簿1")指定具体工作簿，当一个工作簿中包含多个sheet时，使用Sheets("sheet2")指定具体工作表；当只有一个工作簿时，可以直接获取单元格值，此处工作簿为当前工作簿，工作表为第一个默认表sheet1。

   ```python
   OurExcelApp = win32.GetActiveObject("Excel.Application")
   RangeSelect = OurExcelApp.Range("A1:L5001").Value
   RangeSelect = OurExcelApp.Sheets("sheet2").Range("A1:L5001").Value
RangeSelect=OurExcelApp.Workbooks("RawData.xlsx").Sheets("sheet2").Range("A1:L5001").Value
   ```
   
   