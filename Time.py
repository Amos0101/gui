import time
print(time.ctime(0)) #epoch = when my computer thinks time began
#print(time.time()) # return current seconds since epoch
print(time.ctime(time.time()))

time_object = time.localtime()
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
#print(local_time)

#year , month, day, hours, minutes, seconds, day of the week, day of the year,dst

time_tuple = (2024,5,30,4,53,0,3,0,0)
time_string = time.asctime(time_tuple)
time_secs = time.mktime(time_tuple)

print(local_time
      )