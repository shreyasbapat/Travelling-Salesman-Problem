import numpy as np
from random import shuffle, randrange
from time import time
from numba import jit

N_ITER = 2


def algorithm(cities):
    best_order = []
    best_length = float('inf')
    print("We are here!")
 
    for i in range(N_ITER):
        order =  [int(i) for i in range(cities.shape[0])]
        shuffle(order)
        length = calc_length(cities, order)
        start = time()
        print("Yep")
        changed = True
        while changed:
            changed = False
            for a in range(-1, cities.shape[0],2):

                for b in range(a+1, cities.shape[0],2):

                    new_order = order[:a] + order[a:b][::-1] + order[b:]
                    new_length = calc_length(cities, new_order)

                    if new_length < length:
                        length = new_length
                        order = new_order
                        changed = True

        if length < best_length:
            best_length = length
            best_order = order
        
    return best_order, best_length

@jit
def calc_length(cities, path):
	length = 0
	for i in range( len(path) ):
		length += (dist_squared( cities[ path[i-1] ], cities[ path[i] ] ))**0.5

	return length

@jit
def dist_squared(c1, c2):
	t1 = c2[0] - c1[0]
	t2 = c2[1] - c1[1]

	return t1**2 + t2**2
