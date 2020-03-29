import threading

def hello(num):
    for i in range(num):
        print('Hello')

def hi(num):
    for i in range(num):
        print('Hello')

t1 = threading.Thread(target=hello,args=(5,))
t2 = threading.Thread(target=hi, args=(3,))

t1.start() # start thread 1
t1.join()  # wait until thread 1 is done

t2.start() # start thread 2
t2.join()  # wait until thread 2 is done

print('Thread completed') # both threads executed
