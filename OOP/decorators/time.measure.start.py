from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

t = time()
f()
print('f took:', time() - t) # f took: 0.3003859519958496

t = time()
g()
print('g took: ', time() - t )