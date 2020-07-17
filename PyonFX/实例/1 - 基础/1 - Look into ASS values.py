"""
此脚本展示了您从输入ASS文件中获得的ASS值。

首先你需要创建一个Ass对象，它将帮助你管理输入/输出。
一旦创建，它将自动从输入的 .ass 文件中
提取所有信息。

更多使用 Ass 类 的信息: 
https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html#pyonfx.ass_core.Ass

通过执行这个脚本，你会看到ASS里有什么,
例如视频分辨率一样、样式、行等 都存储在对象和列表中。
理解它很重要，因为这些 Python 列表、对象
将贯穿您编写 KFX 的整个过程

不要为如此巨大的输出担心，即使是像这个文件夹中
那个小的输入文件，也有很多信息。

您可以在此处找到每个用于表示输入 .ass 文件对象的更多信息：
https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html
"""
from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()

#print( meta )
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
#print( styles )
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
#print( lines )
for line in lines:
	print(line)