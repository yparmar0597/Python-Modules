### Generator & Iterator

def sqr(x):
    for i in range (1, 1+x):
        yield i*i

a = sqr(3)
# Generator sequences
print(next(a))
print(next(a))
print(next(a))

### Iterator operation
iter_list=iter(['A','B','C'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))