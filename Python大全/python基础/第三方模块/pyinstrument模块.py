# distutils: language=3
# cython: language_level=3
# -*- coding: utf-8 -*-
# @Time    : 2024/2/4 16:47
# @Author  : dujufei-jk
# @Description: 查看代码的子函数运行时间
# 安装：pip install pyinstrument -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

from pyinstrument import Profiler
profiler = Profiler()
profiler.start()
# 这里是你要分析的代码
profiler.stop()
profiler.print()