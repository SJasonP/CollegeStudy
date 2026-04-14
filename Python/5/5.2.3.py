# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
Python的字典可以用于模拟现实生活中的字典。
想出你在前面课程中学习过的5个编程术语，将它们作为字典中的键，并将它们的含义作为字典中的值。
打印每个术语及其含义，注意换行。
"""

D = {
    "print": "标准打印输出指定内容",
    "str": "将指定内容强制转换为字符串格式",
    "int": "将指定内容强制转换为整数格式",
    "range": "总是在各种地方都有用的整数生成器",
    "input": "标准获取用户输入内容"
}

for i in D:
    print(i, ": ", D[i])