#!/usr/bin/python3

from setuptools import setup

setup(
    name='screen-cap',
    version='0.1.0',
    description='录屏软件',
    author='hai2007',
    author_email='2501482523@qq.com',
    url='https://github.com/hai2007/screen-cap',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'basic-toolkit>=0.2.0',
        'wxPython>=4.1.1',
        'pillow>=9.0.1',
        'opencv-python>4.5.5.64',
        'pyautogui>=0.9.53',
        'moviepy>=1.0.3'
    ]
)
