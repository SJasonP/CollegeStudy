# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个至少包含5个用户名的列表，并且其中一个用户名为'root'（其余4个用户名自定义）。
编写代码，在每个用户登录网站后都打印一条问候消息。
用户名如果为root的用户和其余四个用户的问候消息不一样。
"""


def do_hello(username):
    if username == "root":
        print("Welcome back, captain. All system online.")
    else:
        print(f"Welcome back, {username}!")


users = ["root", "_daemon", "sjasonp", "guest"]

for u in users:
    do_hello(u)
