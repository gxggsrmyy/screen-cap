#!/usr/bin/python3

from basic_toolkit import type
import wx
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as pyag

class ScreenCap(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Screen Cap")
        panel = wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)

        begin_btn=  wx.Button(panel, label='开始') # 添加开始按钮
        begin_btn.Bind(wx.EVT_BUTTON, self.doStart)
        sizer.Add(begin_btn, 0, wx.ALL|wx.CENTER, 5)

        stop_btn=  wx.Button(panel, label='结束')  # 添加结束按钮
        stop_btn.Bind(wx.EVT_BUTTON, self.doStop)
        sizer.Add(stop_btn, 0, wx.ALL|wx.CENTER, 5)

        panel.SetSizer(sizer)
        self.Show()

        self._flag=True

    def doStart(self, event):
        fourcc=cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        out=cv2.VideoWriter('output.avi',fourcc,30,pyag.size()) # 参数分别为 输出文件名，解码方式，帧数，录像范围--当前为全屏模式

        while(True):
            img=ImageGrab.grab()
            img_np=np.array(img)
            frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) # ImageGrab获取的颜色为BGR排序，需转换为RGB
            out.write(frame)
            cv2.imshow('screen',frame)
            if not(self._flag): # 结束条件
                break
        out.release()
        cv2.destroyAllWindows()


    def doStop(self, event):
        self._flag=False


if __name__ == '__main__':

    # 创建一个程序
    app=wx.App()

    frame=ScreenCap()

    # 运行主程序
    app.MainLoop()
