import numpy as np
from random import shuffle, randrange
from time import time


def algorithm(cities, distances, n):
    best_order = []
    best_length = float('inf')

    if(n < 200):
        N_ITER = 10
    elif(n >= 200 and n < 400):
        N_ITER = 4
    else:
        N_ITER = 1

    for i in range(N_ITER):
        order = [int(i) for i in range(cities.shape[0])]
        shuffle(order)
        length = calc_length(cities, order, distances)
        start = time()
        changed = True
        while changed:
            changed = False
            for a in range(-1, cities.shape[0]):

                for b in range(a+1, cities.shape[0]):

                    new_order = order[:a] + order[a:b][::-1] + order[b:]
                    new_length = calc_length(cities, new_order, distances)

                    if new_length < length:
                        length = new_length
                        order = new_order
                        changed = True
                        print(*order)
        if length < best_length:
            best_length = length
            best_order = order

    return best_order, best_length


def calc_length(cities, path, distances):
    length = 0
    for i in range(len(path)):
    length += distances[path[i-1]][path[i]]
    return length
