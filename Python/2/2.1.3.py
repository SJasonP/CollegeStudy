# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
想想可存储到列表中的东西，如山川、河流、国家、城市、语言或你喜欢的任何东西，
编写一个程序，在其中创建一个包含这些元素的列表。
把上课介绍的有关列表的函数都使用一遍来处理这个列表
"""

langs = ["Chinese", "English", "French"]
langs.sort()
print(langs)
langs.reverse()
print(langs)
print(len(langs))
for i in langs:
    print(i)