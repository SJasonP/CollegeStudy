# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
对于下面列出的各种情况，至少编写两个条件测试，结果分别为False和True。
检查两个字符串是否相等和不等；
使用lower()方法的条件测试；
涉及相等、不等、大于、小于、大于等于和小于等于的数值比较；
使用关键字and和or的条件测试；
测试特定的值是否在列表中；
测试特定的值是否不在列表中。
"""

print("China" == "America")
print("People" == "People")

print("America".lower() == "America")
print("People".lower() == "people")

print(2 == 1)
print(1 == 1)
print(1 != 1)
print(2 != 1)
print(1 > 2)
print(2 > 1)
print(2 < 1)
print(1 < 2)
print(1 >= 2)
print(1 >= 1)
print(2 <= 1)
print(1 <= 1)

print(True and False)
print(True and True)
print(False or False)
print(False or True)

print("a" in ["a", "b", "c"])
print("d" in ["a", "b", "c"])