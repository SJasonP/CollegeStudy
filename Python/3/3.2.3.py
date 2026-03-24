# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
自定义一个列表，使用两个for循环，将列表中的每个元素都打印出来。
"""

L = ["Gavin", "Sanka", "Jaxx", "Cupertino", "California", "New York", "Minecraft", "Interstellar"]

for i in range(len(L) // 2):
    print(L[i], end=", ")

for i in range(len(L) // 2, len(L)):
    print(L[i], end=", ")
