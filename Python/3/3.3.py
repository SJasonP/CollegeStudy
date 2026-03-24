# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
想出你最喜欢的5种食物、电影、游戏（任选一种都可以），并将其存储在一个元组中。
使用一个for循环将元组中的元素都打印出来；
尝试修改其中一个元素，观察Python报错信息；
调整一下元组元素，替换两个元素。请编写一行给元组变量赋值的代码，并使用一个for循环将新元组的每个元素都打印出来。
"""

T = ("Minecraft", "Subnautica", "Orwell: Keeping An Eye on You", "Detroit: Become Human")

print()
for i in T:
    print(i, end=", ")
print()
print()
try:
    T[0] = "Edge Surf"
except Exception as e:
    print(e)

T = ("Minecraft", "Subnautica", "Hacknet", "Unheard")

print()
for i in T:
    print(i, end=", ")
