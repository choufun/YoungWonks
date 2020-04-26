'''
Design an algorithm to multiply two input numbers and display the results

E.g. to time

* python3 -m timeit '[print(x) for x in range(100)]'
    100 loops, best of 3: 11.1 msec per loop
    
* python3 -m timeit '[print(x) for x in range(10)]'
    1000 loops, best of 3: 1.09 msec per loop
    We can see that the time per loop changes depending on the input!

'''

import time

def multiply1(a,b):
    c = a*b
    return c


def multiply2(a,b):
    return a*b


start_time = time.time()
a = int(input('Enter A: '))
b = int(input('Enter B: '))
print(multiply1(a,b))
print("--- %s seconds ---\n" % (time.time() - start_time))


start_time = time.time()
print(multiply2(int(input('Enter A: ')),int(input('Enter B: '))))
print("--- %s seconds ---\n" % (time.time() - start_time))
