# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个列表，其中包含1——10这10个整数的立方，再使用一个for循环将这些立方数打印出来
"""

nums = []

for i in range(1, 11):
    nums.append(i * i * i)

for i in nums:
    print(i, end=" ")
