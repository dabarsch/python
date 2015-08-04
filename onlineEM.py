import numpy as np

## Functions ##

def addMeasure(measure, count = 1, subCount = 1, mea1 = 'occ', mea2 = 'free'):
	if measure == 'alt':
		for i in range(count):
			if i % 2 == 0:
				addMeasure(mea1, subCount)
			else:
				addMeasure(mea2, subCount)
	else:
		measurements.append(measure)
		quantity.append(count)

# Map measurement to matrix
def getObs(measure):
	if measure == 'occ':
		return 0
	elif measure == 'free':
		return 1
	elif measure == 'no':
		return 2
	else:
		raise ValueError('Unspecified measurement was used')

def updateParam(measure):
	calcGamma(measure)
	calcPhi(measure)
	updateA
	calcQ()

def calcGamma(measure):
	denom = 0
	for l in range(n):
		for h in range(n):
			gamma_[l][h] = A_[l][h] * B_[h][measure]
			denom += gamma_[l][h] * Q_[l]

	for l in range(n):
		for h in range(n):
			gamma_[l][h] /= denom

def calcPhi(measure):
	_old_phi = phi_.copy()
	for i in range(n):
		for j in range(n):
			for k in range(m):
				for h in range(n):
					_sum = 0
					for l in range(n):
						_old_phi_l = _old_phi[i][j][k][l]
						if measure == k and i == l and j == h:
							_sum += gamma_[l][h] * (_old_phi_l + eta_ * (Q_[l] - _old_phi_l))
						else:
							_sum += gamma_[l][h] * _old_phi_l * (1 - eta_)
					phi_[i][j][k][h] = _sum

def calcQ():
	Q_old_ = Q_[:]
	for l in range(n):
		Q_[l] = 0
		for m in range(n):
			Q_[l] += gamma_[m][l] * Q_old_[m]

def calcA():
	for i in range(n):
		_denom = 0
		_sum = np.zeros([n])
		for j in range(n):
			for k in range(m):
				for h in range(n):
					_sum[j] += phi_[i][j][k][h]
			_denom += _sum[j]
		for j in range(n):
			A_[i][j] = _sum[j] / _denom

def calcB():
	for j in range(n):
		_denom = 0
		_sum = np.zeros([m])
		for k in range(m):
			for i in range(n):
				for h in range(n):
					_sum[k] += phi_[i][j][k][h]
			_denom += _sum[k]
		for k in range(m):
			B_[j][k] = _sum[k] / _denom

## Initialization ##

measurements = []
quantity = []

n = 2
m = 3

eta_ = 0.001

A_ = [[	0.9,	0.1],
	  [	0.1,	0.9]]

B_ = [[	0.7,	0.2,	0.1],
	  [ 0.2,	0.7,	0.1]]

Q_ = [	0.5,	0.5]

gamma_ = np.zeros([n, n])
phi_ = np.ones([n, n, m, n]) * 1e-10

## Measurement inputs ##

# High dynamic
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	2)
# addMeasure(	 'free', 	1000)
# addMeasure(	 'occ', 	50)

# Semi staic
addMeasure(	 'alt', 	100, 100)
addMeasure(	 'occ', 	4)

# Static occ
# addMeasure(	 'occ', 	10000)
# addMeasure(	 'free', 	60)

# main()
for i in range(len(measurements)):
	for j in range(quantity[i]):
		measure = getObs(measurements[i])
		calcGamma(measure)
		calcQ()
		calcPhi(measure)
		calcA()
		#calcB()
		print Q_
