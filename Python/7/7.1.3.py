# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
让用户输入一个整数，并指出这个数是否是10的整数倍。
"""

num = 0
try:
    num = int(input("来输入一个整数试试："))
except:
    print("别没事找事，爱用不用。")
    exit()

if num % 10 == 0:
    print(num, "是 10 的整数倍")
else:
    print(num, "和 10 看起来没啥关系")