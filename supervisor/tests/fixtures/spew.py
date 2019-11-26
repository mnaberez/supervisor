#!<<PYTHON>>
import time

counter = 0

while counter < 30000:
   time.sleep(0.01)
   print("more spewage %s" % counter)
   counter += 1
