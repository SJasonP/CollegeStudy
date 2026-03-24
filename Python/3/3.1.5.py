# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个列表，其中包含3——30内能被3整除的数，再使用一个for循环将这个列表中的数打印出来
"""

nums = []

for i in range(3, 31):
    if i % 3 == 0:
        nums.append(i)

for i in nums:
    print(i, end=" ")
