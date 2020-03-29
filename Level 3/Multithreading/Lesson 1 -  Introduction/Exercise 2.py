import threading
import timeit

def hello(num):
    for i in range(num):
        print('Hello')

def hi(num):
    for i in range(num):
        print('Hello')

t1 = threading.Thread(target=hello,args=(5,))
t2 = threading.Thread(target=hi, args=(3,))

start1 = timeit.default_timer()
t1.start() # start thread 1

start2 = timeit.default_timer()
t2.start() # start thread 2

t1.join()
print(round(timeit.default_timer()-start1,4),end='s\n')

t2.join()
print(round(timeit.default_timer()-start2,4),end='s\n')

print('Thread completed') # both threads executed
