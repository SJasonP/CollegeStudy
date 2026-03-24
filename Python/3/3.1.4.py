# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
通过range()函数指定第三个参数来创建一个列表，其中包含1——20的奇数；
再使用一个for循环将这些数打印出来。
"""

nums = [i for i in range(1, 21, 2)]
for i in nums:
    print(i, end=" ")
