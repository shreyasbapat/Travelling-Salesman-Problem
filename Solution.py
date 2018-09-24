"""
CS562 - Artificial Intelligence
-------------------------------

Assignment 1

-> Shreyas Bapat (B16145)
-> Niraj Yadav (B16024)
"""
from graph import Graph
# import os
# os.chdir("TestCases/")
# filenames = ["euc_100", "euc_250", "euc_500", "noneuc_100", "noneuc_250", "noneuc_500"]

# f=open("euc_100", "r")



eu = input()
if eu=="euclidean":
    euclid = True
else:
    euclid = False

n = int(input())

g = Graph(n)


coordinates = []
for _ in range(n):
    x = [float(i) for i in input().split()]
    coordinates.append(x)

distances = []
for _ in range(n):
    x = [float(i) for i in input().split()]
    distances.append(x)

g.graph = distances

g.primMST()
