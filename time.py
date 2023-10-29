import time
current_time = time.time()
print(current_time)

local_time = time.ctime(current_time)
print ("The local time is:", local_time)