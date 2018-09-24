"""
CS562 - Artificial Intelligence
-------------------------------

Assignment 1

-> Shreyas Bapat (B16145)
-> Niraj Yadav (B16024)
"""
from graph import Graph
import numpy as np
import os
os.chdir("TestCases/")
filenames = ["euc_100", "euc_250", "euc_500", "noneuc_100", "noneuc_250", "noneuc_500"]

f=open("euc_100", "r")
eu = f.readline().split()[0]
print (eu)

if eu=="euclidean":
    euclid = True
else:
    euclid = False

n = f.readline()
n=int(n)
g = Graph(n)

i=0
coordinates = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    coordinates.append(x)
    
i=0
distances = []
for i in range(n):
    x = [f.readline().split()]
    x = [float(i) for i in x[0]]
    distances.append(x)

print(coordinates)
print(distances)


g.graph = distances

g.primMST()


