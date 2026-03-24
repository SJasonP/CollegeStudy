# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个包含数1——1000000的列表，再使用一个for循环将这些数打印出来
"""

nums = [i for i in range(1, 1000001)]
for i in nums:
    print(i, end=" ")
