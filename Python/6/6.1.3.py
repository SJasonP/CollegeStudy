# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
在之前的程序中你调查过部分同学最喜欢的歌，这些同学的名字已经在字典中，而其他同学的名字不在字典中。
遍历这个名单，对于已参与调查的同学，打印一条消息表示感谢；对于未参与调查的同学打印一条邀请消息。
"""

d = {
    "John": "Counting Stars",
    "Jason": ""
}
# 假定空白即为没有参与

for n in d:
    if d[n]:
        print("感谢", n, "参与调查！")
    else:
        print("欢迎", n, "来参与调查！")