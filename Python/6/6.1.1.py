# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
在上一个作业—“编程术语”的字典中中再次添加5个python编程术语，再次遍历此字典。
"""

D = {
    "print": "标准打印输出指定内容",
    "str": "将指定内容强制转换为字符串格式",
    "int": "将指定内容强制转换为整数格式",
    "range": "总是在各种地方都有用的整数生成器",
    "input": "标准获取用户输入内容",
    "for": "制造出精妙的循环",
    "while": "制造出死板的循环",
    "keys": "键值对中的“键”",
    "values": "键值对中的“值”",
    "items": "键值对中的“对”"
}

for i in D:
    print(i, ": ", D[i])