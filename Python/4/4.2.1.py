# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
假设玩家在游戏中消灭了一个NPC，请创建一个名为npcs的变量，存放NPC的名字，将其赋值为‘paimeng’、'naxidan'、'kaya'。(此处同学们可以自定义)
编写一条if语句，测试NPC的名字是否为'naxidan'(根据你的变量值来设定条件，下同)。如果是，就打印一条消息，指出玩家获得了5分。
编写这个程序的两个版本，上述条件测试在其中一个版本中通过，在另一个版本中未通过（未通过条件测试时没有输出）。
"""

# The names are from Lord of Mysteries
npcs = ["Amon", "Alger Wilson", "Leonard Mitchell"]


npc = "Alger Wilson"
if npc == "Amon":
    print("获得了5分！")