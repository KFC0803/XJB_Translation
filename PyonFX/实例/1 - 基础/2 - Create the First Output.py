"""
此脚本在 "Output.ass" 创建了第一个对话行, 这是
输出的默认名称，它包含了原来的对话行（已勾选注释）+ 新生成的行。

神奇的函数是write_line()，一个Ass的类函数
它将Line类的对话行转换回文本格式并将其添加到“Output.ass”中。
更多详细信息，请访问: https://pyonfx.readthedocs.io/en/latest/reference/ass%20utility.html#pyonfx.ass_utility.Ass.write_line

为了展示第一个操作，我们取输入文件的第一行
只更改其文本，并把它输出。

这不是一个好方法，因为原始行的文本被覆盖了
对于接下来的操作，您将无法再获取该行的原始值
只能通过创建一个新的Ass对象来重新读取输入文件。

相反，您应该始终创建一个行的副本以保留原始行，我们将在下面的示例中看到如何创建。

最后，您必须调用 save() 类来实际写入输出。
PyonFX还将自动Print您已写入的行数和进程持续时间。
更多详细信息，请访问: https://pyonfx.readthedocs.io/en/latest/reference/ass%20utility.html#pyonfx.ass_utility.Ass.save

最后，调用 open_aegisub 来在Aegisub打开输出。一般来说，您要是更愿意
用MPV打开的话，可以选择调用 open-MPV ，然而示例的ass文件没有视频。
更多详细信息，请访问:
- open_aegisub: https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html#pyonfx.ass_core.Ass.open_aegisub
- open_mpv: https://pyonfx.readthedocs.io/en/latest/reference/ass%20core.html#pyonfx.ass_core.Ass.open_mpv
"""
from pyonfx import *

io = Ass("in.ass")
meta, styles, lines = io.get_data()

lines[0].text = "I am a new line!"
io.write_line(lines[0])

io.save()
io.open_aegisub()