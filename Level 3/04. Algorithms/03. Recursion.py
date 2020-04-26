import time

'''
Function loop with recursion

'''

def recursion():
    print("...the function called within itself to create a loop...")
    recursion()


'''
Conventional Fibonacci Method

'''

def fibonacci1():
    a=1
    b=1
    c=None
    
    while True:
        if a  == 233:
            break
        print(a)
        c=a+b
        a=b
        b=c
        time.sleep(0.5)
#fibonacci1()


'''
Recursive Fibonacci Method

'''

def fibonacci2(a,b):
    if a == 233:
        return
    print(a)
    time.sleep(0.5)
    fibonacci2(b,a+b)
#fibonacci2(1,1)


'''
Recursive Factorial Method

'''

def factorial(n):
    if n == 1:
       return 1 
    return factorial(n-1)*n
#print(factorial(5))


'''
Coventional Pascal's Triangle Method

'''
def pascal1():
    print(1)
    layer = [1,1]
    layers = 1
    while layers < 10:
        for elem in layer:
            print(elem,end=' ')
        print()
        new_layer = []
        for i in range(len(layer)-1):
            num1 = layer[i]
            num2 = layer[i+1]
            new_layer.append(num1+num2)
        new_layer=[1]+new_layer+[1]
        layer=new_layer
        layers+=1


'''
Recursive Pascal's Triangle Method

'''

def pascal2(layer):
    if len(layer)>10:
        return
    for e in layer:
        print(e,end=' ')
    print()
    new=[]
    for n in range(len(layer)-1):
        new.append(layer[n]+layer[n+1])
    new = [1]+new+[1]
    pascal2(new)
print(1)
pascal2([1,1])
    
