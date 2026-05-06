# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
每个同学都有多个自己喜欢的数字，把每个同学的名字及其喜欢的数字存储起来，
然后将每个人的名字及其喜欢的数打印出来。
"""

nums = {
    "Jason": 7,
    "Sanka": 3,
    "Gavin": 5
}

for n in nums:
    print(n, "最喜欢", nums[n])