# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
创建一个包含数1——1000000的列表，在使用min()和max()核实该列表确实是从1开始，到1000000结束的。
另外，对这个列表调用函数sum()，看看python将100万个数相加需要多长时间。
"""

nums = [i for i in range(1, 1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))
