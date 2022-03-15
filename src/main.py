#!/usr/bin/python3

from basic_toolkit import type
import wx

class ScreenCap(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Screen Cap")
        panel = wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)

        # 添加开始按钮
        begin_btn=  wx.Button(panel, label='开始')
        begin_btn.Bind(wx.EVT_BUTTON, self.doStart)
        sizer.Add(begin_btn, 0, wx.ALL|wx.CENTER, 5)

        # 添加结束按钮
        stop_btn=  wx.Button(panel, label='结束')
        stop_btn.Bind(wx.EVT_BUTTON, self.doStop)
        sizer.Add(stop_btn, 0, wx.ALL|wx.CENTER, 5)

        panel.SetSizer(sizer)
        self.Show()

    def doStart(self, event):
        print("开始")

    def doStop(self, event):
        print("结束")


if __name__ == '__main__':

    # 创建一个程序
    app=wx.App()

    frame=ScreenCap()

    # 运行主程序
    app.MainLoop()
