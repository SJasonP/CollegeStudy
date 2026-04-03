# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
将上一题中的if-else结构改为if-elif-else结构
如果NPC为paimeng，就打印一条消息，指出玩家获得了5分。
如果NPC为naxidan，就打印一条消息，指出玩家获得了10分。
如果NPC为kaya，就打印一条消息，指出玩家获得了15分。
"""

# The names are from Lord of Mysteries
npcs = ["Amon", "Alger Wilson", "Leonard Mitchell"]

npc = "?"

if npc == "Leonard Mitchell":
    print("获得了5分！")
elif npc == "Alger Wilson":
    print("获得了10分！")
elif npc == "Amon":
    print("获得了15分！")
else:
    print("暂未得分。")