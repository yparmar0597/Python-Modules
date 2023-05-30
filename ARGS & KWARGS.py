### ARGS & KWARGS

# *args example:

def sum(*args):
    total = 0
    for i in args:
        total += i
    print(total)

sum(1,2,3,4,5,6,7,8,9)  


#  *kwargs example:

def show(**kwargs):
    print(kwargs)

show(A=1, B=2, c=3)    