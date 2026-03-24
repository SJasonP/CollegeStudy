# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建上题的列表副本，并将其赋给变量new_list，再完成如下任务：
在原来列表中添加一个元素（自定义）；
在new_list列表中添加另外一个元素（自定义，和原来列表中添加的不一样即可）；
核实有两个不同的列表。使用for循环分别打印两个列表，观察结果。
"""

a_list = ["Cupertino", "California"]
new_list = a_list

a_list.append("New York")
new_list.append("London")

for i in a_list:
    print(i, end=" ")

print()
for i in new_list:
    print(i, end=" ")
