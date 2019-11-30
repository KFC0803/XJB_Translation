# 安装

这篇是我折腾出来的，官方的一键方法我没法使用。。。

1.克隆https://github.com/CoffeeStraw/PyonFX

2.找到setup.py，将27行改为

```python
    long_description=open('README.md', encoding= 'utf-8').read(),
```
3.在文件夹中打开cmd(如果你的Python安装的时候选了“所有人安装”，就以管理员身份运行cmd，cd到这个文件夹)，执行

```
python setup.py build
pip install pyquaternion
pip install sphinx_rtd_theme
pip install sphinx_rtd_theme
python setup.py install
```
完成
