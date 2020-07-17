
# `class pyonfx.ass_core.Meta`

## Meta对象包含了Ass的信息

## 可以在此获取它们的更多信息:<http://docs.aegisub.org/manual/Styles>

`wrap_style`

决定字幕行如何换行

类型:int

`scaled_border_and_shadow`

确定是否使用脚本分辨率(True)或视频分辨率(False)来缩放边框和阴影

类型:bool

`play_res_x`

视频宽度

类型:int

`play_res_y`

视频高度

类型:int

`audio`

加载的音频的绝对路径

类型:str

`video`

加载的视频的绝对路径

类型:str

# `class pyonfx.ass_core.Style`

## Style对象包含一组应用于对话行的排版格式规则

## 可以在此获取样式的更多信息: <http://docs.aegisub.org/3.2/ASS_Tags/>

`fontname`

字体名

类型:str

`fontsize`

字体大小（点数）

类型:float

`color1`

主要颜色

类型:str

`alpha1`

主要颜色的透明度

类型:str

`color2`

次要颜色（用于kalaoke效果）

类型:str

`alpha2`

次要颜色的透明度

类型:str

`color3`

边框颜色

类型:str

`alpha3`

边框颜色的透明度

类型:str

`color4`

阴影颜色

类型:str

`alpha4`

阴影颜色的透明度

类型:str

`bold`

字体是否加粗

类型:bool

`italic`

字体是否为斜体

类型:bool

`underline`

字体是否有下划线

类型:bool

`strikeout`

字体是否有删除线

类型:bool

`scale_x`

文本水平缩放

类型:float

`scale_y`

文本垂直缩放

类型:float

`spacing`

字间距

类型:float

`angle`

旋转角度

类型:float

`border_style`

是否是不透明背景

类型:bool

`outline`

边框厚度

类型:float

`shadow`

阴影距离

类型:float

`alignment`

对齐方式

类型:int

`margin_l`

左边框距离

类型:int

`margin_r`

右边框距离

类型:int

`margin_v`

垂直边框距离

类型:int

`encoding`

字符编码

类型:int

# `class pyonfx.ass_core.Line`

## Line对象包括了Ass中每一行的信息

### 提示

### (*) = 此项仅在 extended = True 时有效

`i`

行索引值

类型:int

`comment`

是否为注释行。如果为True，这行将不会在屏幕上显示。

类型:bool

`layer`

行的层号。层号较高的行将显示在层号较低的行上方。

类型:int

`start_time`

行开始时间（毫秒）

类型:int

`end_time`

行结束时间（毫秒）

类型:int

`duration`

行持续时间（毫秒）

类型:int

`leadin`

行前时间（毫秒，首行为 1000.1）(*)

类型:float

`leadout`

行后时间（毫秒，首行为 1000.1）(*)

类型:float

`style`

此行使用的样式名称

类型:str

`styleref`

此行的Style对象的引用 (*)

类型:obj

`actor`

说话人

类型:str

`margin_l`

该行的左边距

类型:int

`margin_r`

该行的右边距

类型:int

`margin_v`

该行的垂直边距

类型:int

`effect`

特效

类型:str

`raw_text`

该行的原始文本

类型:str

`text`

该行的文本（无标签）

类型:str

`width`

行文本宽度(*)

类型:float

`height`

行文本高度(*)

类型:float

`ascent`

该行上方距离 (*)

类型:float

`descent`

该行下方距离 (*)

类型:float

`internal_leading`

中心 (*)

Line font internal lead (*).

类型:float

`external_leading`

外围 (*)

Line font external lead (*).

类型:float

`x`

行水平坐标（取决于对齐方式）(*)

类型:float

`y`

行垂直坐标（取决于对齐方式）(*)

类型:float

`left`

行左横坐标 (*)

类型:float

`center`

行中心横坐标 (*)

类型:float

`right`

行右横坐标 (*)

类型:float

`top`

行顶部纵坐标 (*)

类型:float

`middle`

行中心纵坐标 (*)

类型:float

`bottom`

行底部纵坐标 (*)

类型:float

`words`

包含此行内Word对象的列表 (*)

类型:list

`syls`

包含此行内Syllable对象的列表(如果有) (*)

类型:list

`chars`

包含此行内Char对象的列表 (*)

类型:list

`copy()`

返回：一个此对象的深度副本（行）

# `class pyonfx.ass_core.Word`

## word对象包含了Ass中一行的单个单词的信息

## word可以是一些文本，在其前后都有一些可选的空格（e.g.:在字符串“What a beautiful world!”中，“beautiful” 和 “world”都是不同的单词）

`i`

单词索引值

类型:int

`start_time`

单词开始时间（与行开始时间相同）（毫秒）

类型:int

`end_time`

单词结束时间（与行结束时间相同）（毫秒）

类型:int

`duration`

单词持续时间（与行持续时间相同）（毫秒）

类型:int

`styleref`

此对象原始行的Style对象的引用

类型:obj

`text`

单词文本

类型:str

`prespace`

单词前的空格

类型:int

`postspace`

单词后的空格

类型:int

`width`

单词文本宽度

类型:float

`height`

单词文本高度

类型:float

`x`

单词水平坐标（取决于对齐方式）

类型:float

`y`

单词垂直坐标（取决于对齐方式）

类型:float

`left`

单词左横坐标

类型:float

`center`

单词中心横坐标

类型:float

`right`

单词右横坐标

类型:float

`top`

单词上部纵坐标

类型:float

`middle`

单词中心纵坐标

类型:float

`bottom`

单词底部纵坐标

类型:float

classpyonfx.ass_core.Syllable
Syllable object contains informations about a single syl of a line in the Ass.

A syl can be defined as some text after a karaoke tag (k, ko, kf) (e.g.: In “{k0}Hel{k0}lo {k0}Pyon{k0}FX {k0}users!”, “Pyon” and “FX” are distinct syllables),

i
Syllable index number

Type:	int
word_i
Syllable word index (e.g.: In line text “{k0}Hel{k0}lo {k0}Pyon{k0}FX {k0}users!”, syl “Pyon” will have word_i=1).

Type:	int
start_time
Syllable start time (in milliseconds).

Type:	int
end_time
Syllable end time (in milliseconds).

Type:	int
duration
Syllable duration (in milliseconds).

Type:	int
styleref
Reference to the Style object of this object original line.

Type:	obj
text
Syllable text.

Type:	str
tags
All the remaining tags before syl text apart k ones.

Type:	str
inline_fx
Syllable inline effect (marked as -EFFECT in karaoke-time).

Type:	str
prespace
Syllable free space before text.

Type:	int
postspace
Syllable free space after text.

Type:	int
width
Syllable text width.

Type:	float
height
Syllable text height.

Type:	float
x
Syllable text position horizontal (depends on alignment).

Type:	float
y
Syllable text position vertical (depends on alignment).

Type:	float
left
Syllable text position left.

Type:	float
center
Syllable text position center.

Type:	float
right
Syllable text position right.

Type:	float
top
Syllable text position top.

Type:	float
middle
Syllable text position middle.

Type:	float
bottom
Syllable text position bottom.

Type:	float