"""
CS562 - Artificial Intelligence
-------------------------------

Assignment 1

-> Shreyas Bapat (B16145)
-> Niraj Yadav (B16024)
"""

import math
from plot import plot
#from aco import ACO, Graph
#from graph import Graph
from travel import algorithm
from time import time
import numpy as np
#import os
import itertools
#os.chdir("TestCases/")
#filenames = ["euc_100", "euc_250", "euc_500", "noneuc_100", "noneuc_250", "noneuc_500"]

f=open("euc_100", "r")
eu = f.readline().split()[0]
# print (eu)

if eu=="euclidean":
    euclid = True
else:
    euclid = False

n = int(f.readline())

# g = Graph(n)

coordinates = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    coordinates.append(x)
    
distances = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    distances.append(x)

# print(coordinates)
# print(distances)


# g.graph = distances

# m = g.primMST()

# x = g.dictiseMST(m)

# print(x)

# print(list(x.values()))

# merged = list(itertools.chain.from_iterable(list(x.values())))

# print(merged)

# merged.sort()

# print(x[0])


start = time()
path, length = algorithm(coordinates,n)
algorithm(cities)
print(path)
#length = pow(length,0.5)
plot(coordinates,path)
tottime = time() - start
print( "Found path of length %s in %s seconds" % ( round(length,2), round(tottime, 2) ) )

