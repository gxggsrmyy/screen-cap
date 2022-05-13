#!/usr/bin/python3

from basic_toolkit import type
import wx
import os
import saveVideo
import time

class ScreenCap(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Screen Cap", size=wx.Size(300, 140))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        begin_btn = wx.Button(panel, label='开始')  # 添加开始按钮
        begin_btn.Bind(wx.EVT_BUTTON, self.doStart)
        sizer.Add(begin_btn, 0, wx.ALL | wx.CENTER, 5)

        stop_btn = wx.Button(panel, label='结束')  # 添加结束按钮
        stop_btn.Bind(wx.EVT_BUTTON, self.doStop)
        sizer.Add(stop_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)
        self.Show()

    def doStart(self, event):
        self.VideoInstance = saveVideo.New()  # 开始录制视频

    def doStop(self, event):
        self.VideoInstance.doStop()  # 停止录制视频

        time.sleep(1)
        os._exit(0)


if __name__ == '__main__':

    # 创建一个程序
    app = wx.App()

    frame = ScreenCap()

    # 运行主程序
    app.MainLoop()
