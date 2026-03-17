# Author: SJasonP <SJasonP@iCloud.com>
# Repo: https://github.com/SJasonP/CollegeStudy

import os
import time

if __name__ == "__main__":
    for i in range(5):
        print("正在打开第" + str(i+1) + "个QQ……")
        time.sleep(0.5)
        os.system("open /Applications/QQ.app/Contents/MacOS/QQ")
        time.sleep(0.5)
    print("任务完成！")