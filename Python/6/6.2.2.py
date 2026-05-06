# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
使用两个字典分别存储你和你好朋友的信息，包括姓名、年龄、籍贯等（可以自行设定其他属性），
再将这两个字典都存储在一个名为people的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来。
"""

people = [
    {
        "name": "Jason",
        "age": 18,
        "from": "China"
    },
    {
        "name": "Gavin",
        "age": 18,
        "from": "China"
    }
]

for i in people:
    print(i)
