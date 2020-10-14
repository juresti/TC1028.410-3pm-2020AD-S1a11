import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

uno = time.perf_counter()
time.sleep(1)
dos = time.perf_counter()
print(uno, dos)