# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
模拟网站如何确保每个用户的用户名都为唯一。
创建一个至少包含5个用户名（英文字符，不要包含中文字符）的列表，并将其命名为current_users。
再创建一个包含5个用户名（英文字符，不要包含中文字符）的列表，将其命名为new_users，并确保其中有一两个用户名也在列表curren_users中。
遍历列表new_users，检查其中的每个用户名是否被使用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
确保比较时不区分大小写。即如果用户名‘ZangSan’已被使用，应拒绝‘ZHANGSAN’。（提示：根据提议创建列表current_users的副本，其中包含当前所有用户名的小写版本）
"""

current_users = ["root", "_daemon", "postgres", "sjasonp", "guest"]
new_users = ["PostGres", "jaxx", "gavin", "sanka", "guest"]

for user in new_users:
    if user.lower() in current_users:
        print("请更换其它的用户名。")
    else:
        print("用户名未被使用。")
