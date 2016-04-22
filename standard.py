##################################
# Akshat Agrawal and Joseph Hostyk
# CS 124
# Programming Assignment 3
# 4/25/16
#
# standardRepresentaition.py
##################################


import random
import math
import time


maxIter = 25000

def createRandNumFile():
	f = open("50randNums.txt", "w")
	for i in range (0, 101):
		f.write(str(random.randint(0,math.pow(10, 12)))+"\n")
	f.close()

def kk(ns):
	# rename so that the array itself isn't edited
	nums = list(ns)
	while(len(nums)>1):
		#print "i"
		max1 = max(nums)
		max1index = nums.index(max1)
		nums[max1index] = 0
		max2 = max(nums)
		nums[max1index] = max1-max2
		nums.remove(max2)
	return nums[0]


# Output random array of {-1,1} of size n
def randMove(n):
	return [random.choice([1,-1]) for i in range(0,n)]

# Compute the residue when using standard representation
# Input: nums = array of nums; sol = array of 1s and -1s
# Output: residue
def stdResidue(nums, sol):
	residue = 0
	for i in range(len(nums)):
		residue += nums[i]*sol[i]
	return abs(residue)

# Takes in a solution, gives a random neighbor solution
def randNeighbor(sol):
	# copy so that we don't edit the original array
	neighbor = list(sol)
	# choose 2 random indices:
	toSwap = random.sample(range(0,len(neighbor)), 2)
	# flip one of them
	neighbor[toSwap[0]] *= -1
	# with probability 1/2, also flip the other
	if (random.choice([0,1])== 0):
		neighbor[toSwap[1]] *= -1
	return neighbor

# Run repeated random on input nums, and return the best
# residue it can find.
def repeatedRandom(nums):
	t0 = time.time()
	bestSol = randMove(len(nums))
	bestResidue = stdResidue(nums, bestSol)
	for i in range(0, maxIter):
		testSol = randMove(len(nums))
		testResidue = stdResidue(nums, testSol)
		if(testResidue < bestResidue):
			bestSol = testSol
			bestResidue = testResidue
	return (bestResidue, time.time()-t0)

# Run hill-climbing on input nums, and return the best
# residue it can find.
def hillClimbing(nums):
	t0 = time.time()
	bestSol = randMove(len(nums))
	bestResidue = stdResidue(nums, bestSol)
	for i in range(0, maxIter):
		# print "Current Best: {}".format(bestResidue)
		testSol = randNeighbor(bestSol)
		testResidue = stdResidue(nums, testSol)
		# print "New: {}".format(testResidue)
		if(testResidue < bestResidue):
			bestSol = testSol
			bestResidue = testResidue
	return (bestResidue, time.time()-t0)


# Run simulated annealing on input nums, and return the best
# residue it can find.
def simulAnnealing(nums):
	t0 = time.time()
	# travelSol will walk around the map. This is S in the pset
	travelSol = randMove(len(nums))
	travelResidue = stdResidue(nums, travelSol)
	# bestSol is the best solution we've found so far. This is S''
	bestSol = travelSol
	bestResidue = travelResidue
	for i in range(0, maxIter):
		# testSol is a neighbor. This is S'
		testSol = randNeighbor(travelSol)
		testResidue = stdResidue(nums, testSol)
		if(testResidue < travelResidue):
			travelSol = testSol
			travelResidue = testResidue
		elif (random.random() < math.exp((0-testResidue-travelResidue)/(pow(10,10)*pow(0.8,i/300.0)))):
			travelSol = testSol
			travelResidue = testResidue
		if (travelResidue < bestResidue):
			bestSol = travelSol
			bestResidue = travelResidue
	return (bestResidue, time.time()-t0)


if __name__ == '__main__':
	inputfile = "50randNums.txt"
	#inputfile = "testNums.txt"
	f = open(inputfile, "r")
	nums = [int(a) for a in f]
	f.close()

	# print "KK: {}, rand: {}, HC: {}, SA: {}".format(kk(nums), repeatedRandom(nums), hillClimbing(nums), simulAnnealing(nums))
	#prepartition([10,8,7,6,5])
	# print kk(nums)
	r, t = repeatedRandom([10,8,7,6,5])
	print r
	print t
	# print repeatedRandom(nums)
	# print hillClimbing(nums)
	# print simulAnnealing([10,8,7,6,5,99,1,52,58,20,80,10,90,8,8,7,7,50,25,25,10,8,2])



