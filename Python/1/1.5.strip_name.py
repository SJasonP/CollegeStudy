# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
删除人名中的空白：用变量表示你自己的名字，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。

打印名字，显示其开头和末尾的空白。然后，分别使用lstrip()、rstrip()、strip()对人名进行处理，并将结果打印出来
"""

name = "\t\n  Jason Pan  \n\t"
print("原始名字（显示空白）:")
print(repr(name))
print("原始名字直接打印:")
print(name)
print("\n使用lstrip()去除左边空白:")
print(repr(name.lstrip()))
print("使用rstrip()去除右边空白:")
print(repr(name.rstrip()))
print("使用strip()去除两端空白:")
print(repr(name.strip()))