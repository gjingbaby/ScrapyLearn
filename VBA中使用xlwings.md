# VBA中使用xlwings

## 1.加载xlwings到VBA

在python版本中安装xlwings情况下：

1. cmd中执行xlwings addin install，重启excel后选项卡中会显示xlwing选项卡。
2. VBA界面中，工具>引用，勾选xlwings。         

**注意事项**

- 文件层面，会在C:\Users\Administrator\AppData\Roaming\Microsoft\Excel\XLSTART下，出现文件xlwings.xlam(宏文件)，此文件是由在python安装xlwings库过程中存储在C:\Python37\Lib\site-packages\xlwings\addin目录下的xlwings.xlam文件复制而来。
- xlwings.xlam(宏文件)作为xlwings安装包的一部分，随版本更新，并可以在github/xlwings/release中找到。

## 2.在VBA中调用python代码

1. 准备好py代码，并存储成py文件。
2. 在vba中调用，vba代码所在xlam文件与py文件在同一目录。
3. 以下分别是py代码和vb代码。

```python
import random
import xlwings as xw

def vbatest():
    wb = xw.Book(r"C:\Users\Administrator\Desktop\world.xlsm")
    sht = wb.sheets["sheet1"]

    headline = ["名称","编号"]
    sht.range("A1:B1").value = headline

    column_mc = random.sample(range(1,100000),10000)
    column_bh = random.sample(range(1,50000),10000)
    sht.range("A2").options(transpose=True).value = column_mc
    sht.range("B2").options(transpose=True).value = column_bh

```

```vb
Option Explicit

Sub PythonUseInVba()
    RunPython ("import mc;mc.vbatest()")
End Sub
```

**注意事项**

1. 在vba中引用时，使用函数RunPython，参数为str格式。
2. 首先引入py文件名称，再通过py文件名称调用函数。
3. 通过在excel中执行宏，展示py文件的结果。
4. **目标是在提供给其他人使用时易用，可以给按钮加载宏。**

