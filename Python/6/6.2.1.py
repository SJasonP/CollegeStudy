# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。
将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息打印出来。
"""

pets = [
    {
        "type": "猫",
        "master": "张三"
    },
    {
        "type": "狗",
        "master": "李四"
    },
    {
        "type": "鸟",
        "master": "王五"
    }
]

for i in pets:
    print("这只", i["type"], "是", i["master"], "的。")