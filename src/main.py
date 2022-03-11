#!/usr/bin/python3

from basic_toolkit import type
import wx

# 创建一个程序
app=wx.App()

# 创建一个窗口
frame=wx.Frame(None,title="Screen Cap")

# 显示结果
frame.Show()

# 运行主程序
app.MainLoop()
