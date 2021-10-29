#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
from progressbar import *
filep='Z:\\codedown\\AndroidR\\out\\target\\product\\redi\\vendor\\bin\\hw\\dtvkitserver' # 文件路径

# print( os.path.getatime(file) )   # 输出最近访问时间
# print( os.path.getctime(file) )   # 输出文件创建时间
# print( os.path.getmtime(file) )   # 输出最近修改时间
# print( time.gmtime(os.path.getmtime(file)) )  # 以struct_time形式输出最近修改时间
# print( os.path.getsize(file) )   # 输出文件大小（字节为单位）
# print( os.path.abspath(file) )   # 输出绝对路径
# print( os.path.normpath(file) )  # 规范path字符串形式
dtv1 = os.path.getmtime(filep)


pbar = ProgressBar().start()
# total = 300
# if len(sys.argv) > 1:
total = int(sys.argv[1])
count = 0
while(count < total):
    dtv2 = os.path.getmtime(filep)
    if dtv1 != dtv2:
        count = total - 1
        pbar.update(int((count / (total - 1)) * 100))
        # print("updtv\n")
        os.system("D:\\tool\\upload.bat")
    else:
        time.sleep(1)
        pbar.update(int((count / (total - 1)) * 100))
    count += 1


