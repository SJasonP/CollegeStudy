# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

s = input("ENTER A STRING: ")
d = {}

for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

print(d)