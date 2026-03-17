# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
想出至少三部你最喜欢的电影，将其名字存储在一个列表中，再使用for循环将每部电影的名称打印出来。
修改这个for循环，使其打印包含电影名称的句子，而不仅仅是电影的名字，每部电影都显示一行输出；
在程序末尾添加一行代码（不在for循环中），指出你有多喜欢电影，输出需要包含针对每部电影的字符串，还要有一个总结性的句子。
"""

movies = [
    "Interstellar",
    "The Shawshank Redemption",
    "Who Am I: No System Is Safe"
]

print()
for movie in movies:
    print(movie)

quotes = [
    "Mankind was born on Earth. It was never meant to die here.",
    "Hope is a good thing, maybe the best of things, and no good thing ever dies.",
    "The biggest vulnerability in any system is the human."
]

print()
for i in range(len(movies)):
    print(movies[i] + ":\n\t" + quotes[i])

print()
print("电影让没有想象力、看不懂书籍的人也能体验到奇妙的世界和人生……这就是我认为的电影伟大之处。")
print("\t《星际穿越》打开宇宙与情感的宏大，")
print("\t《肖申克的救赎》打开人性与信念的坚韧，")
print("\t而《我是谁》则打开数字时代混乱世界的迷宫。")
print("我喜欢电影，大概就是喜欢被这些钥匙打开的过程——\n"
      "在别人的故事里，遇见一部分新的自己，然后带着这点星光，回到现实里继续前行。")
