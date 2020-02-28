# VBA基础语法

## 1.基础语法

**注意事项**

1）储存成启用宏的工作簿，即xlsm格式

2）安全性方面，信任中心建议设置成禁用所有宏，并发出通知

3）工具选项中设置字体，其中带有chinese的才会正常显示汉字，选项中需要设置要求变量声明，方便调试

4）代码在模块中编辑，可插入模块，模块名称在其下方的属性中直接修改

5）VBA语言属于面向对象语言，即Object.action类型

6）自定义功能区，打开开发工具选项卡

```vb
Sub Create_A_Worksheet()
    '面向对象编程oop，object.action
    '创建sheet表
    Worksheets.Add
   
    '单元格赋值
    Range("A1").Value = "日期"
    Range("B1").Value = "门店"
    Range("C1").Value = "销售额"
    Range("D1").Value = "门店损耗"
    Range("E1").Value = "商品1销量"
    
    '获取用户信息，填入表格
    Range("B2").Value = Environ("UserName")  '获取环境的用户名，就是计算机名
    Range("A2").Value = Date  '获取当前时间
    
    '格式调整
    Range("A1:E1").Font.Color = vbBlue  '字体颜色
    Range("A1:E1").Interior.Color = vbYellow   '单元格颜色
    
End Sub
```

## 2.Debug

1）Syntax Errors (语法错误）
2）Compile Errors （编译错误）
3）Runtime Errors (运行错误)

**注意事项**

1.工具选项中勾选要求变量声明

2.使用调试模式，逐行调试，断点调试

3.运行前可先进行编译

## 3.代码使用

1）使用开发工具下宏，点击执行，选项中可设置快捷键

2）插入形状，对象添加宏，点击形状可执行

3）自定义快速访问工具栏，excel顶部

4）功能区中，自定义选项卡（同开始，插入这些）

