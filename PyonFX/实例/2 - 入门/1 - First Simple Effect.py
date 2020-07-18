"""
在这里我们有了第一个完整的特效。
如你所见，我们现在已经填满了romaji, kanji 和 sub 函数。

先从简单的开始，sub 函数使用行前时间和行后时间来适应行与行之间的变化。
随后我们构建每一行的文本，给定an（对齐方式）、pos（坐标）和fad（淡入淡出）来使入场和退场丝般顺滑。
	(Docs: https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html#pyonfx.ass_core.Line.leadin)

在 romaji 函数中，我们要构建一个针对音节的效果。
为此，每一个音节都得是一个对话行，
所以，我们循环遍历当前行的音节。
我们用了 Utils 模块中的一个实用程序，all_non_empty()，
因为我们知道我们不需要用到空白的或持续时间为0的音节。
	(Docs: https://pyonfx.readthedocs.io/en/latest/reference/utils.html#pyonfx.utils.Utils.all_non_empty)

类似于 sub 函数，我们用 fad 标签制作了淡入淡出的效果，
然后我们用一个简单的变换构建了第一个主要效果，得到了一个伸长/收缩效果。

记住一定要为行设置层数。通常，主要效果应有一个比入场和退场更高的值，
因为主要效果更重要，所以这样能使这些行显示在其他效果上方。

对于kanji函数，您会发现这就是从 romaji 函数里面复制过来的，
但是使用的是 char 而不是 syl。请尝试如果 kanji 用 syl 会怎么样！
"""

from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()

def romaji(line, l):
	for syl in Utils.all_non_empty(line.syls):
		# Leadin Effect
		l.layer = 0

		l.start_time = line.start_time - line.leadin/2
		l.end_time = line.start_time + syl.start_time
		l.dur = l.end_time - l.start_time

		l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
			syl.center, syl.middle, line.leadin/2, syl.text)

		io.write_line(l)

		# Main Effect
		l.layer = 1

		l.start_time = line.start_time + syl.start_time
		l.end_time = line.start_time + syl.end_time
		l.dur = l.end_time - l.start_time
		
		l.text = "{\\an5\\pos(%.3f,%.3f)"\
				 "\\t(0,%d,0.5,\\1c&HFFFFFF&\\3c&HABABAB&\\fscx125\\fscy125)"\
				 "\\t(%d,%d,1.5,\\fscx100\\fscy100\\1c%s\\3c%s)}%s" % (
			syl.center, syl.middle,
			l.dur/3, l.dur/3, l.dur, line.styleref.color1, line.styleref.color3, syl.text)
		
		io.write_line(l)

		# Leadout Effect
		l.layer = 0

		l.start_time = line.start_time + syl.end_time
		l.end_time = line.end_time + line.leadout/2
		l.dur = l.end_time - l.start_time

		l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
			syl.center, syl.middle, line.leadout/2, syl.text)

		io.write_line(l)

def kanji(line, l):
	for char in Utils.all_non_empty(line.chars):
		# Leadin Effect
		l.layer = 0

		l.start_time = line.start_time - line.leadin/2
		l.end_time = line.start_time + char.start_time
		l.dur = l.end_time - l.start_time

		l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
			char.center, char.middle, line.leadin/2, char.text)

		io.write_line(l)

		# Main Effect
		l.layer = 1

		l.start_time = line.start_time + char.start_time
		l.end_time = line.start_time + char.end_time
		l.dur = l.end_time - l.start_time
		
		l.text = "{\\an5\\pos(%.3f,%.3f)"\
				 "\\t(0,%d,0.5,\\1c&HFFFFFF&\\3c&HABABAB&\\fscx125\\fscy125)"\
				 "\\t(%d,%d,1.5,\\fscx100\\fscy100\\1c%s\\3c%s)}%s" % (
			char.center, char.middle,
			l.dur/3, l.dur/3, l.dur, line.styleref.color1, line.styleref.color3, char.text)
		
		io.write_line(l)

		# Leadout Effect
		l.layer = 0

		l.start_time = line.start_time + char.end_time
		l.end_time = line.end_time + line.leadout/2
		l.dur = l.end_time - l.start_time

		l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
			char.center, char.middle, line.leadout/2, char.text)

		io.write_line(l)

def sub(line, l):
	# Translation Effect
	l.start_time = line.start_time - line.leadin/2
	l.end_time = line.end_time + line.leadout/2
	l.dur = l.end_time - l.start_time

	l.text = "{\\fad(%d,%d)}%s" % (
		line.leadin/2, line.leadout/2, line.text)

	io.write_line(l)

for line in lines:
	# Generating lines
	if line.styleref.alignment >= 7:
		romaji(line, line.copy())
	elif line.styleref.alignment >= 4:
		kanji(line, line.copy())
	else:
		sub(line, line.copy())

io.save()
io.open_aegisub()