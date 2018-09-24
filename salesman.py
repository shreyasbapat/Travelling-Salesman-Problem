__author__ = "Shreyas Bapat" 

from travel import algorithm
import numpy as np
from time import time
from random import randint

screenSize = 700

def main():
	#loading data
	f = open("datasets/tsp0100.txt", 'r').read().splitlines()
	numCities = f.pop(0)
	cities = np.array([ tuple( map( float, coord.split() ) ) for coord in f ])
	
	#calculating path
	start = time()
	path, length = algorithm( cities )
	# algorithm(cities)
	print(path)

	tottime = time() - start
	print( "Found path of length %s in %s seconds" % ( round(length,2), round(tottime, 2) ) )

	#displaying path
	# drawPath( path, cities, length )

################################ DRAWING METHODS #################################

if __name__ == "__main__":
	main()
