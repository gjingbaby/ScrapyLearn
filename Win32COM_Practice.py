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
