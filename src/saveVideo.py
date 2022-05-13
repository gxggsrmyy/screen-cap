#!/usr/bin/python3

from basic_toolkit import type
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as pyag
import _thread


class New():
    def __init__(self):
        self._flag = True
        _thread.start_new_thread(self.doit, (self,))

    def doit(self, args):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        # 参数分别为 输出文件名，解码方式，帧数，录像范围--当前为全屏模式
        out = cv2.VideoWriter('output.avi', fourcc, 30, pyag.size())

        while(True):
            img = ImageGrab.grab()
            img_np = np.array(img)
            # ImageGrab获取的颜色为BGR排序，需转换为RGB
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if not(self._flag):  # 结束条件
                break
        out.release()
        cv2.destroyAllWindows()
        print('录制视频结束~')

    def doStop(self):
        self._flag = False
