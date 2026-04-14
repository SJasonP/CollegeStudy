# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
在上一题的程序中添加一条if语句，检查用户名列表是否为空。
如果为空，就打印如下消息：暂无用户！
为了确保消息能够打印，删除列表中的所有用户。
"""


def do_hello(username):
    if username == "root":
        print("Welcome back, captain. All system online.")
    else:
        print(f"Welcome back, {username}!")


users = ["root", "_daemon", "sjasonp", "guest"]
users = []

if users:
    for u in users:
        do_hello(u)
else:
    print("暂无用户！")
