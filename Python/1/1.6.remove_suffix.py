# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

"""
文件扩展名：请将一个文件名（包含扩展名，如：notes.txt）赋值给变量filename，再使用removesuffix()方法来显示不包含扩展名的文件名。
"""

filename = "SJasonP-ReadMe.md"
name_without_extension = filename.removesuffix('.md')
print(f"原始文件名: {filename}")
print(f"去除扩展名后: {name_without_extension}")