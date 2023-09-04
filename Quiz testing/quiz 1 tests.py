print(len("95637+12"))

def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=12)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)