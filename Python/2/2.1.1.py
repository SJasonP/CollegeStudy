# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
想出至少5个你最想去旅游的地方。
将这些地方存储在一个列表中，按原始顺序打印该列表；
使用sorted()按字母顺序打印这个列表，不要修改它；
再次打印该列表，核实排列顺序未变；
使用sorted()按与字母顺序相反的顺序打印这个列表，不要修改它；
再次打印该列表，核实排列顺序未变；
使用reverse()修改列表元素的排列顺序，打印该列表，核实排列顺序确实变了；
使用reverse()再次修改列表元素的排列顺序，打印该列表，核实已回复到原来的排列顺序；
使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了；
使用sort()修改该列表，使其元素按字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
"""

places = ["Cupertino", "New York", "London", "Singapore", "Somewhere"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)