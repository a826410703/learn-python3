import os
import datetime,time


os.chdir(r'E:\yunjian\华夏银行信用卡中心\20160413')
ds=list(os.listdir())
for d in ds:
    if os.path.isfile(d):
        os.remove(d)
    else:
        shutil.rmtree(d)

dirDe=r'E:\yunjian\华夏银行信用卡中心\soft\linkfs-bin-110211'

ds1=list(os.walk(dirDe))
deltime=datetime.timedelta(days=5)
now=datetime.datetime.now()

for d in ds1:
    os.chdir(d[0])
    if d[2] !=[]:
        for x in d[2]:
            ctime=datetime.datetime.fromtimestamp(
                os.path.getctime(x)
            )
            if ctime<(now-deltime):
                os.remove(x)
            else:
                pass
