# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
使用一个字典来存储你的朋友喜欢的歌。
至少写出5个同学名字，将这些同学名字作为字典中的键，将这些同学喜欢的歌作为字典中的值。
打印每个同学的名字和他（她）喜欢的歌名。
为了使程序更有趣，使用本班同学的真实姓名，通过询问同学确保数据真实性。
"""

d = {
    "王五": "戒不掉",
    "张三": "沉溺",
    "李四": "李白",
    "老六": "兰亭序",
    "Jason": "Collapsing World"
}

for n in d:
    print(n, "like listening to", d[n])
