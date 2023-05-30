### Multiprocessing

# Multiprocessing Import:-

import multiprocessing
import time

def print_cube(num):
    print("Cube: {}".format(num**3))

def print_square(num):
    print("Square: {}".format(num**2))


if __name__=="__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10, ))  # declaration of process
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))

    start = time.time()
    p1.start()
    p2.start()
    # wait until p1 gets finished
    p1.join()
    p2.join()
    # Both processes are finished
    end = time.time()
    print("Done in {} duration!!!".format(end-start))