# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
编写一个程序，询问用户有多少人用餐。
如果超过8个人，就打印一条消息，打印出没有空桌；否则就打印出有空桌。
"""
num = 0
try:
    num = int(input("有多少人用餐？："))
except:
    print("你这啥回答？不吃拉倒")
    exit()

if num <= 0:
    print("来踢馆的是不是？几个意思啊")
elif num > 8:
    print("实在抱歉，没有足够的空桌，您另去别家吧？")
else:
    print("没问题！我们有足够的空桌。")
