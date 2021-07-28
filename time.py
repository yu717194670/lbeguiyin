import time
 
def shijianchuo(ms):
	timeStamp = ms / 1000
	timeArray = time.localtime(timeStamp)
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	print(otherStyleTime)

shijianchuo(1627467349288)