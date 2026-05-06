# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个字典，在其中存储三条河流（城市、山川等）及所在的国家。如，一个键值对为‘huanghe’: ‘china’。
使用循环为每条河流（城市或山川等，根据自己定义的字典写）打印一条消息，如：
   The Huanghe runs through China.
使用循环将该字典中的每条河流的名字打印出来
使用循环将该字典包含的每个国家的名字打印出来
"""

rivers = {
    "Nile River": "Egypt",
    "Amazon River": "Brazil",
    "Mississippi River": "US"
}

for r in rivers:
    print("The", r, "runs through", rivers[r])