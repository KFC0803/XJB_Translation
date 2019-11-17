
# Quick Start Guide

********************************


首先，你需要知道你要如何进行创作。你需要了解（如果你还不知道的话）如下内容：

 - **ASS格式** Pyonfx仍然是一个高级的排版工具和卡拉OK特效（karaokers）工具，它应该被经验丰富的用户（typesetters）使用，他们知道Libass所提供的所有标签。检查脚注以获得所有标签的完整列表。
 - **Python3脚本语言** 像Python这样的编程语言可以让你定义在某种情况下你想要什么、多久一次、应用于这个或那个……总得来说能使你更自由。在一个完全图形化的界面中，你将不局限于只有几个命令的按钮、滑块或文本字段。**基本上就是这样**。变量、函数、条件、循环、比较、字符串格式化、列表和字典……你可以在脚注中找到一些优秀教程的链接。

要开始生成，你只需像以前那样在Python 3中编写脚本，它将描述你的KFX或高级排版创作的一切（process）。

总之，如果你还没**安装Python 3**，你可以从[官网][1]上**下载它**。如果你是Windows系统，请确保选中“Add Python 3.x to PATH”复选框。这使得你不需要进行额外操作来使Python可以在cmd中被调用。

如果你还不会安装Python，你可以从网上找点教程，比如 https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624

## 安装

运行如下命令，该命令将使用pip安装并更新库：
```
pip install --upgrade https://github.com/CoffeeStraw/PyonFX/zipball/master
```

或者，如果由于某种原因（例如你不使用Windows上，或者同时装了Python2及Python3）而无法运行:
```
pip3 install --upgrade https://github.com/CoffeeStraw/PyonFX/zipball/master
```
好了。一切准备就绪，当你需要更新时，就再运行一次上面的命令

## 安装-额外步骤

这一步不需要用到此库。但就我个人而言，Aegisub太老/太臃肿了，我需要一种更舒适的工作方式。

这就是为什么PyonFX集成了一种额外的方式，你可以更快地在修改软字幕之后使用[MPV播放器][2]预览你的作品。如果你*不*使用Windows，安装它就足够了。

如果你正使用Windows上，只要你安装了它（去网站上找），你要做的就是把它添加到 PATH 中，这样库就可以使用它了。你可以在[这里][3]找到一些指导。

你需要添加包含mpv的.exe的文件夹到PATH中，通常是C:\Program Files\mpv。

## 开始

你可能想检查一下现在一切是否正常。为此，我建议你尝试运行一些在[项目github官方仓库][4]中的示例。

要在Python中运行脚本，只需运行以下命令：
```
python namefile.py
```

或者，如果由于某种原因（例如你不使用Windows上，或者同时装了Python2及Python3）而无法运行:
```
python3 namefile.py
```

我强烈建议你生成并研究examples文件夹中的每个示例（从[这里][5]下载最新的）。这些都是为零基础初学者进阶为高级用户准备的，并详细解释了库中所有相关函数的用法。

## Tips

 - 不要一口气做一个KFX。休息一下，散散步，从周围环境中寻求灵感；
 - 选择视频元素。你的效果应以某种方式与背景契合；
 - 考虑人类的认知。我们主要关注运动，其次是对比度，然后是颜色。效果太多会让人头疼，少了又很无聊；
 - 使用现代风格来升华（光，曲线，粒子，渐变），用旧风格来增强可读性（纯色，粗边框，静态位置）；
 - 如果背景太华丽，请尝试插入面板形状*(panel shape)*，以将文本置于“安全地带”中；
 - 适应卡拉OK时间和声音*(voice)*。快歌没有音节持续时间，不适合使用需要一些时间才能看到的效果。

### 脚注

 - ASS标签大全 http://docs.aegisub.org/3.2/ASS_Tags/
 - 推荐的Python3 教程:
Italian: https://github.com/AllenDowney/ThinkPythonItalian/blob/master/thinkpython_italian.pdf
English: http://greenteapress.com/thinkpython2/thinkpython2.pdf
（不是我推荐的——译者注）

  [1]: https://www.python.org/downloads/
  [2]: https://mpv.io/
  [3]: https://jingyan.baidu.com/article/8ebacdf02d3c2949f65cd5d0.html
  [4]: https://github.com/CoffeeStraw/PyonFX/tree/master/examples
  [5]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/CoffeeStraw/PyonFX/tree/master/examples
  [5]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/CoffeeStraw/PyonFX/tree/master/examples
