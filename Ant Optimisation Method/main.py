import math

from aco import ACO, Graph
#from plot import plot
from time import time

f=open("euc_500", "r")
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

def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main():
    """
    cities = []
    points = []
    with open('./data/euc_500') as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
            points.append((int(city[1]), int(city[2])))
    cost_matrix = []
    rank = len(cities)
    #print(cities)
    #print(rank)
    """
    rank=n
    cost_matrix = []
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distances[i][j])
        cost_matrix.append(row)
        #print(row)
    start = time()
    #print(rank)
    aco = ACO(2, 100, 1.0, 10, 10, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    print('cost: {}, path: {}'.format(cost, path))
    tottime = time() - start
    #plot(points, path)
    print('TotalTime : ', tottime)
if __name__ == '__main__':
    main()
