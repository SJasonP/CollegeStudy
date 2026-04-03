# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
设置变量age的值，再编写一个if-elif-else结构，根据age的值判断这个人处于人生的那个阶段。
如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
如果年龄为2岁（含）-4岁，就打印一条消息，指出这个人是幼儿。
如果年龄为4岁（含）-13岁，就打印一条消息，指出这个人是儿童。
如果年龄为13岁（含）-18岁，就打印一条消息，指出这个人是少年。
如果年龄为18岁（含）-65岁，就打印一条消息，指出这个人是中青年人。
如果年龄达到65岁，就打印一条消息，指出这个人是老年人。
"""

age = 18

if age < 2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 18:
    print("少年")
elif age < 65:
    print("中青年人")
else:
    print("老年人")