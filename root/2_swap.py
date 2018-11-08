"""
CS562 - Artificial Intelligence
-------------------------------
Assignment 1
-> Shreyas Bapat (B16145)
-> Niraj Yadav (B16024)
"""
from base import algorithm
import numpy as np
eu = input()

n = int(input())
coordinates = []
for i in range(n):
    x = [float(i) for i in input().split()]
    x = []
    coordinates.append(x)

distances = []
for i in range(n):
    x = [float(i) for i in input().split()]
    distances.append(x)

coordinates = np.array(coordinates)
distances = np.array(distances)
path, length = algorithm(coordinates,distances,n)
print(*path)
