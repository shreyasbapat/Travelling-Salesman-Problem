import math
import random
from node import *
import numpy as np
from sys import stdout
from time import time

l_min = None
pic = 0
xmin=0
ymin=0
xmax=0
ymax=0
indent = 4
nn = 0
anim = False

def optimize2opt(nodes, solution, number_of_nodes):
    best = 0
    best_move = None
    for ci in range(0, number_of_nodes):
        for xi in range(0, number_of_nodes):
            yi = (ci + 1) % number_of_nodes
            zi = (xi + 1) % number_of_nodes

            c = solution[ ci ]
            y = solution[ yi ]
            x = solution[ xi ]
            z = solution[ zi ]

            cy = length( c, y )
            xz = length( x, z )
            cx = length( c, x )
            yz = length( y, z )

            if xi != ci and xi != yi:
                gain = (cy + xz) - (cx + yz)
                if gain > best:
                    best_move = (ci,yi,xi,zi)
                    best = gain

    if best_move is not None:
        (ci,yi,xi,zi) = best_move
        c = solution[ ci ]
        y = solution[ yi ]
        x = solution[ xi ]
        z = solution[ zi ]

        new_solution = [int(i) for i in range(0,number_of_nodes)]

        new_solution[0] = solution[ci]

        n = 1

        while xi != yi:
            new_solution[n] = solution[xi]
            n = n + 1
            xi = (xi-1)%number_of_nodes
        new_solution[n] = solution[yi]

        n = n + 1
        while zi != ci:
            new_solution[n] = solution[zi]
            n = n + 1
            zi = (zi+1)%number_of_nodes
        return (True,new_solution)
    else:
        return (False,solution)


def sa_optimize_step(nodes, dist, solution, number_of_nodes, t):
    global nn
    ci = random.randint(0, number_of_nodes-1)
    yi = (ci + 1) % number_of_nodes
    xi = random.randint(0, number_of_nodes-1)
    zi = (xi + 1) % number_of_nodes

    if xi != ci and xi != yi:
        c = solution[ci]
        y = solution[yi]
        x = solution[xi]
        z = solution[zi]
        cy = length(dist, c, y)
        xz = length(dist, x, z)
        cx = length(dist, c, x)
        yz = length(dist, y, z)

        gain = (cy + xz) - (cx + yz)
        if gain < 0:
            u = math.exp( gain / t )
        elif gain > 0.05:
            u = 1
        else:
            u = 0

        if (random.random() < u):
            nn = nn + 1
            new_solution = [int(i) for i in range(0,number_of_nodes)]
            new_solution[0] = solution[ci]
            n = 1
            while xi != yi:
                new_solution[n] = solution[xi]
                n = n + 1
                xi = (xi-1)%number_of_nodes
            new_solution[n] = solution[yi]
            n = n + 1
            while zi != ci:
                new_solution[n] = solution[zi]
                n = n + 1
                zi = (zi+1)%number_of_nodes

            return new_solution
        else:
            return solution
    else:
        return solution

def sa_algorithm(nodes, dist):
    ctim = time()
    number_of_nodes = len(nodes)
    solution = [n for n in nodes]
    t = 100

    l_min = total_length( nodes, dist, solution )
    best_solution = []
    i = 0
    while t > 0.1:
        i = i + 1
        x = float(time() - ctim)
        if x>=float(2):
            ssol = ''
            ssol += ' '.join(map(lambda x: str(x.id), solution))
            print(ssol)
            ctim = time()
        solution = sa_optimize_step(nodes, dist, solution, number_of_nodes, t)
        if i >= 200:
            i = 0
            l = total_length( nodes, dist, solution )

            t = t*0.9997

            if l_min is None:
                l_min = l
            elif l < l_min:
                l_min = l
                best_solution = solution[:]
            else:
                pass
    return best_solution

def algorithm(nodes, dist):
    global nn
    global l_min
    number_of_nodes = len( nodes )
    s = sa_algorithm(nodes, dist)
    return s

def read_from_stdin():
    eu = input()

    n = int(input())
    coordinates = []
    for i in range(n):
        x = [float(i) for i in input().split()]
        coordinates.append(x)

    distances = []
    for i in range(n):
        x = [float(i) for i in input().split()]
        distances.append(x)
    return coordinates, distances, n

def read_inputs():
    global xmax, ymax, xmin, ymin
    coordi, distances, node_count = read_from_stdin()
    nodes = []
    i = 0
    while i<len(coordi):
        x = float(coordi[i][0])
        y = float(coordi[i][1])
        if x > xmax: xmax = x
        if y > ymax: ymax = y
        if x < xmin: xmin = x
        if y < ymin: ymin = y
        nodes.append(Node(i, x, y))
        i = i + 1
    return nodes, distances, coordi

def solve():
    random.seed(8111142)
    solution_string = None
    nodes, dist, coordi = read_inputs()
    solution = algorithm(nodes, dist)
    objective = total_length(nodes, dist, solution)
    # solution_string = str(objective) + ' 0\n'
    solution_string = ''
    solution_string += ' '.join(map(lambda x: str(x.id), solution))
    lis = [int(i) for i in solution_string.split()]
    return solution_string, lis, coordi

if __name__ == '__main__':
    # a = timer()
    # a.tic()
    sol, lis, nodes = solve()
    #plot(nodes,lis)
    print (sol)
    # a.toc()
