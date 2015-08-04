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

def updateParam(measure):
	calcGamma(measure)
	calcPhi(measure)
	updateA
	calcQ()

def calcGamma(measure):
	for l in range(len(A_)):
		for h in range(len(A_)):
			gamma[l][h] = A_[l][h]




def calcPhi(measure, gamma):

def calcQ():




## Measurement inputs ##

measurements = []
quantity = []

addMeasure(	 'occ', 	10)
addMeasure(	'free', 	10)
addMeasure(	  'no',      100)
addMeasure(	 'occ', 	0)

## Constatns ##

B = np.matrix([[	0.8, 	0.2,	0.5],
			   [	0.2,	0.8,	0.5]])

B_n = np.matrix([[	0.5, 	0],
				 [	  0,  0.5]])

B_o = np.matrix([[	0.8, 	0],
				 [	  0,  0.2]])

B_f = np.matrix([[	0.2, 	0],
				 [	  0,  0.8]])

## Initialization ##

gamma = []
phi = []

A_ = [[	0.8,	0.2],
	  [	0.1,	0.9]]

B_ = [[	0.7,	0.2,	0.1],
	  [ 0.2,	0.7,	0.1]]

Q_ = [	0.5,	0.5]

Q = np.matrix([0.5, 0.5])

p_of = 0.8
p_fo = 0.1

for i in range(len(measurements)):
	for j in range(quantity[i]):
		Q = Q * getTransition() * getObs(measurements[i])
		Q = Q / Q.sum(axis = 1)
		print Q

print A_
print B_
print Q_
