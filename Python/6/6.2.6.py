# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
修改上面五题中的任意一题，对其进行扩展，添加键和值，调整程序要解决的问题，或改进输出的格式。
"""

nums = {
    "Jason": 7,
    "John": 7,
    "Gavin": 5,
    "Sanka": 3,
    "Jaxx": 3,
    "Tim": 3,
}

count = {}

for n in nums:
    if nums[n] in count:
        count[nums[n]] += 1
    else:
        count[nums[n]] = 1
    print(n, "最喜欢", nums[n])

for c in count:
    print("有", count[c], "个人都喜欢数字", c)