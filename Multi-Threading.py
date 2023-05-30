### Multi-Threading

# Thread Import:-

from threading import Thread
import time

global num
num = 0

# The bottleneck of the code which is CPU bound:
def upgrade(num):
    while num<400000000:
        num += 1

# Creation of multiple threads
t1 = Thread(target=upgrade, args=(num//2, ))
t2 = Thread(target=upgrade, args=(num//2, ))

# MultiThread architecture recording time
start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print("Done in {} duration!!!".format(end-start))