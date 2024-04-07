# non-daemon thread : can't normally kill until finish task

# Daemon thread : a thread that run in the background, not important for program
#          to run, ur program will not wait for daemon threads to complete before exitting
#          daemon third used for : background tasks, waiting for input, long run process.
# daemon thread forced the whole process of thread to control, to kill it if needed

import threading
import time

def Timer():
    print() #new-line
    counter = 0
    while True:
        time.sleep(1)
        counter+=1
        print("Increament Counter :",counter)

starting = threading.Thread(target=Timer) #daemon=True
starting.daemon = True #(starting.setDaemon(true)) old
starting.start()



exit = input("are u wish to exit : " + "\n")

print(starting.daemon) #starting.isDaemon() old