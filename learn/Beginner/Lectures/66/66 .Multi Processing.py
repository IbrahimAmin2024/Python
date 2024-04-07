# Multi-Processing : Runing task in Parallel on Different cpu cores
#                    run All tasks together, Bypass Gil used For Threading.
import threading
# MultiProcessing : Better way for CPU boun Tasks heavy[cpu usage/work/..etc].
#                   using 1 Thread and waiting to finish and then
#                   jump to finish another thread. using Gil.


#Multi-threading :  Better for io bound tasks (waiting around)
#                   using many threads to finish shared work


#Note:
# 1- multiProcessing : Using normal call() / using Process
# 2- multiThread     : Using threading.thread


from multiprocessing import Process, cpu_count
import time

# print(__name__)

# def Starting():
#     print("excuted from main module!")
#
# def Checking():
#
#     if __name__ == "__main__":
#         Starting()
#     else:
#         print("can't excuted from another module!")


# Checking()

# ============

def Counter(num):
    Count = 0
    while Count < num:
        Count+=1


def Starting():

    print(cpu_count()) # used to get the number of CPUs in the system

    first = Process(target=Counter,args=(25000,))
    first.start()
    first.join() # synchronisation, finish above before Continuing code bellow

    second = Process(target=Counter,args=(25000,))
    second.start()
    second.join() # synchronisation, finish above before Continuing code bellow

    third = Process(target=Counter, args=(25000,))
    third.start()
    third.join()  # synchronisation, finish above before Continuing code bellow

    fourth = Process(target=Counter, args=(25000,))
    fourth.start()
    fourth.join()  # synchronisation, finish above before Continuing code bellow

    print("Finished in :",time.perf_counter(),"Seconds.")


def Checking():

    if __name__ == "__main__":
        Starting()


Checking()