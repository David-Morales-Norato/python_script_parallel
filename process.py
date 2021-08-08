#!/home/david-norato/miniconda3/bin/python
import time
import sys

print("arugmentos", sys.argv)

for i in range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
    time.sleep(1)
    print(i)

raise Exception("Test error file")