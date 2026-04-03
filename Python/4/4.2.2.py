# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
同上一题一样设置NPC的名字，存入列表中，并编写一个if-else结构。
如果NPC是paimeng(根据你自己的变量值设定)，就打印一条消息，指出玩家因消灭该NPC获得了5分。
如果NPC不是paimeng，就打印一条消息，指出玩家获得了10分。
编写这个程序的两个版本，在一个版本中将执行if代码块，在另一个版本中将执行else代码块。
"""

# The names are from Lord of Mysteries
npcs = ["Amon", "Alger Wilson", "Leonard Mitchell"]

npc = "Leonard Mitchell"

if npc == "Alger Wilson":
    print("获得了5分！")
else:
    print("获得了10分！")
