"""
是时候着手创作一个特效了。
如果我们想更进一步，最好要组织好我们的代码。

在本例中，您将看到一个特效的结构应该是怎样的。
你可以把这个文件作为你未来特效的模板。
将对行的处理及输出交给函数，这些函数通过传递原始行和副本
被调用，您将在这些函数中编辑特效。
你可以指定一个函数的所有效果。

对齐方式大于等于7的行是罗马音(romaji)行。
剩下的那些中，对齐方式小于等于3的是字幕（翻译）(subtitle/translation)行，
其余的(4, 5, 6)是竖排的汉字(kanji)。

如果你已经看过 Ass 类的文档，你应该已经发现
它包含可一个 vertical_kanji 形参，它会自动
为对齐方式等于4，5，6的行计算出竖排的坐标。如果你不想让 pyon 自动定位
竖排对齐方式的汉字(kanji)，你可以指定这个形参为 False。

请注意，这段代码什么也不会做，因为 romaji, kanji, sub 函数里什么都没有。
我们将在下一个章节: 2 - Beginner 中创建第一个特效。
"""
from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()

def romaji(line, l):
	# 请在这里编写 :D
	pass

def kanji(line, l):
	# 请在这里编写 :)
	pass

def sub(line, l):
	# 请在这里编写 :P
	pass

for line in lines:
	# 生成行
	if line.styleref.alignment >= 7:
		romaji(line, line.copy())
	elif line.styleref.alignment >= 4:
		kanji(line, line.copy())
	else:
		sub(line, line.copy())

io.save()
io.open_aegisub()