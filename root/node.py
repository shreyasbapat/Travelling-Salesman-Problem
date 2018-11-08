import math
import random
import numpy as np

def length(disto, n1, n2):
    """Compute the distance between two nodes"""
    i1 = n1.id
    i2 = n2.id
    return disto[i1][i2]

class Node( object ):
    def __init__( self, id, x, y ):
        self.id  = id
        self.sid = None
        self.x   = x
        self.y   = y
        self.taken = False
        self.cluster = None

    def __str__( self ):
        out = str( self.id ) + " {} {}".format( self.x, self.y )
        return out

#-----------------------------------------------------------------------------
def id2node(nodes, idx0):
    return nodes[idx0]

def total_length(nodes, dist, solution ):
    """Compute the total distrance travelled for the given solution"""
    if  isinstance(solution[0], Node):
        useidx=False
    else:
        useidx=True
    objective = 0
    for index in range(0, len(solution)):
        a=index
        b=(index+1) % len(solution)
        if useidx:
            na=id2node(nodes, solution[a])
            nb=id2node(nodes, solution[b])
        else:
            na=solution[a]
            nb=solution[b]
        objective += length(dist, na, nb)
    return objective

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    print("Done")
