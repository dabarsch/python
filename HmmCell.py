import numpy as np

## Functions ##

def addMeasure(measure, count):
	measurements.append(measure)
	quantity.append(count)

# Map measurement to matrix
def getObs(measure):
	if measure == 'occ':
		return B_o
	elif measure == 'free':
		return B_f
	elif measure == 'no':
		return B_n
	else:
		raise ValueError('Unspecified measurement was used')

def getTransition():
	return np.matrix(	[[ 1 - p_fo,     p_fo],
					     [     p_of, 1 - p_of]])

## Measurement inputs ##

measurements = []
quantity = []

addMeasure(	 'occ', 	10)
addMeasure(	'free', 	10)
addMeasure(	  'no',      100)
addMeasure(	 'occ', 	0)

## Constatns ##

B_n = np.matrix([[	0.5, 	0],
				 [	  0,  0.5]])

B_o = np.matrix([[	0.8, 	0],
				 [	  0,  0.2]])

B_f = np.matrix([[	0.2, 	0],
				 [	  0,  0.8]])

## Initialization ##

Q = np.matrix([0.5, 0.5])

p_of = 0.1
p_fo = 0.1

for i in range(len(measurements)):
	for j in range(quantity[i]):
		Q = Q * getTransition() * getObs(measurements[i])
		Q = Q / Q.sum(axis = 1)
		print Q
