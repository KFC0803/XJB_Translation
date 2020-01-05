"""
让我们更进一步。

在这个脚本中，我们将遍历所有 .ass 中的行，
为每一行创建一个副本（原因请参见上一个示例）
平移2000毫秒，最后将它们写回我们的输出。

有关copy方法的详细信息：
https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html#pyonfx.ass_core.Line.copy
"""
from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()

for line in lines:
	l = line.copy()

	l.start_time += 2000
	l.end_time += 2000
	
	io.write_line(l)

io.save()
io.open_aegisub()