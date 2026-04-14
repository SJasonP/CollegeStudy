# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
使用一个字典来存储你个人的信息，
包括姓名、年龄、籍贯等（可以自行设定其他属性）。
将存储在字典中的每项信息都打印出来。
"""

info = {
    "name": "潘建谌",
    "age": 18,
    "birthmon": "2007-07",
    "country": "China",
    "isDead": False
}

print("姓名：", info["name"])
print("年龄：", info["age"])
print("出生月：", info["birthmon"])
print("国籍：", info["country"])
print("是否死亡：", info["isDead"])