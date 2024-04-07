# Thread : a flow execution. like a separate order of instruction. (Multi processing)
#          it's like a thread takes a turn running to achieve concurrency/Sync
#          this lead to future known as GIL : (Global Interpreter lock),
#          it allows only 1 thread to hold the control of the Python.


# cpu bound : prog/task spend most of it's time waiting for internal events (use cpu)
#             use multiprocessing. (its perform tasks/switched if thread idle)
#             use all threads at once / currently [heavily and lagy cpu performs]

# io bound :  prog/task spend most of it's time waiting for external events
#             (user input, fetch data/web scraping,.....)
#    use multithreading. (its waiting, like sync/ no matter if idle will work with thrads)
#    run events/func Sequentially and not currently

import threading
import time

#io bound
#cpu bound
def wearing_jacket(): #external events: work on our main thread
    time.sleep(2)
    print("wearing jacket..")

def watching_tv(): #external events: work on our main thread
    time.sleep(3)
    print("watching tv..")

def change_channel(): #external events: work on our main thread
    time.sleep(5)
    print("changing channel tv..")

# wearing_jacket()
# watching_tv()
# change_channel()

first = threading.Thread(target=wearing_jacket,args=()) #args=(test,test2,)
first.start()
first.join() #wait synce before continue program running code

second = threading.Thread(target=watching_tv,args=())
second.start()
second.join()

third = threading.Thread(target=change_channel,args=())
third.start()
third.join()

print(threading.active_count())
print(threading.enumerate())
