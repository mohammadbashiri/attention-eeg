import threading
import time

# Define a function for the thread
def myThread1():
    while True:
        time.sleep(.5)
        print 'This is a Thread ', 1

def myThread2():
    while True:
        time.sleep(1)
        print 'Thread ', 2

# Create two threads as follows
try:
    threading.Thread(target=myThread1).start()
    threading.Thread(target=myThread2).start()
except:
   print "Error: unable to start thread"

while True:
   pass