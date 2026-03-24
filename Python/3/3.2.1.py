# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
选择你之前编写的列表的一个程序，在末尾添加几行代码，完成以下任务：
打印消息"one two three items in the list are"，再使用切片打印列表的前三个元素；
打印消息"Three items from the middle of the list are"，再使用切片来打印列表中间的三个元素
打印消息"The last three items in the list are"，再使用切片来打印末尾的三个元素
"""

L = ["Gavin", "Sanka", "Jaxx", "Cupertino", "California", "New York", "Minecraft", "Interstellar",
     "The Shawshank Redemption"]

print()
print("one two three items in the list are")
print(L[:3])

print()
print("Three items from the middle of the list are")
print(L[3:6])

print()
print("The last three items in the list are")
print(L[-3:])
