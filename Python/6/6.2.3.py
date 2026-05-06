# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个名为favorite_places的字典。
在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1—3个地方。
遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
"""

favorites_places = {
    "张三": "黄山",
    "李四": "长城"
}

for n in favorites_places:
    print(n, "最喜欢", favorites_places[n])