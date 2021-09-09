import time
 
def shijianchuo(ms):
	timeStamp = ms / 1000
	timeArray = time.localtime(timeStamp)
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	print(otherStyleTime)

shijianchuo(1631167205824)
# import subprocess
# order='adb devices'        #获取连接设备
# pi= subprocess.run("adb devices",shell=True)