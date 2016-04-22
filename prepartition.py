##################################
# Akshat Agrawal and Joseph Hostyk
# CS 124
# Programming Assignment 3
# 4/25/16
#
# standardRepresentaition.py
##################################


##################################
# Akshat Agrawal and Joseph Hostyk
# CS 124
# Programming Assignment 3
# 4/25/16
#
# kk.py: main functions
##################################

import random
import math
import time

maxIter = 25000


def kk(ns):
	# copy so that the array itself isn't edited
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


# return a random partition of size n
def createRandPartition(n):
	return [random.randint(0,n-1) for i in range(n)]

# Partition nums according to partition.
def partition(ns, partition):
	# copy so that the array itself isn't edited
	nums = list(ns)
	# Go through every possible partition, and add the nums
	# in the same partition together.
	for n in range(0, len(nums)-1):
		# http://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
		indices = [i for i, x in enumerate(partition) if x == n]
		if (indices):
			Sum = 0
			for i in indices:
				Sum += nums[i]
				nums[i] = 0
			nums[indices[0]] = Sum
	return nums

# Returns the residue that kk gets from the partitioned array.
def partitionResidue(nums, sol):
	return kk(partition(nums,sol))

# Takes in a solution, gives a random neighbor solution
def randNeighbor(sol):
	options = range(len(sol))
	# choose random index to swap:
	oldSetIndex = random.choice(options)
	# make sure we don't pick j such that p_i =/= j
	options.remove(sol[oldSetIndex])
	newSet = random.choice(options)
	sol[oldSetIndex] = newSet
	return sol


# Run repeated random on input nums, and return the best
# residue it can find.
def repeatedRandom(nums):
	t0 = time.time()
	bestSol = createRandPartition(len(nums))
	bestResidue = partitionResidue(nums, bestSol)
	for i in range(0, maxIter):
		testSol = createRandPartition(len(nums))
		testResidue = partitionResidue(nums, testSol)
		if(testResidue < bestResidue):
			bestSol = testSol
			bestResidue = testResidue
	return (bestResidue, time.time()-t0)


# Run hill-climbing on input nums, and return the best
# residue it can find.
def hillClimbing(nums):
	t0 = time.time()
	bestSol = createRandPartition(len(nums))
	bestResidue = partitionResidue(nums, bestSol)
	for i in range(0, maxIter):
		testSol = randNeighbor(bestSol)
		testResidue = partitionResidue(nums, testSol)
		if(testResidue < bestResidue):
			bestSol = testSol
			bestResidue = testResidue
	return (bestResidue, time.time()-t0)


# Run simulated annealing on input nums, and return the best
# residue it can find.
def simulAnnealing(nums):
	t0 = time.time()
	# travelSol will walk around the map. This is S in the pset
	travelSol = createRandPartition(len(nums))
	travelResidue = partitionResidue(nums, travelSol)
	# bestSol is the best solution we've found so far. This is S''
	bestSol = travelSol
	bestResidue = travelResidue
	for i in range(0, maxIter):
		# testSol is a neighbor. This is S'
		testSol = randNeighbor(travelSol)
		testResidue = partitionResidue(nums, testSol)
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
	# inputfile = "testNums.txt"
	f = open(inputfile, "r")
	nums = [int(a) for a in f]
	f.close()

	# print "KK: {}, rand: {}, HC: {}, SA: {}".format(kk(nums), repeatedRandom(nums), hillClimbing(nums), simulAnnealing(nums))
	#prepartition([10,8,7,6,5])
	# print kk(nums)
	# print repeatedRandom([10,8,7,6,5])
	# print repeatedRandom(nums)
	# print hillClimbing(nums)
	print simulAnnealing(nums)	
	# print simulAnnealing([10,8,7,6,5,99,1,52,58,20,80,10,90,8,8,7,7,50,25,25,10,8,2])



	# assert (partition([10,8,7,6,5],[1,2,2,4,5]) == [10,15,0,6,5])
	# assert (partition([1,2,3,4,5,6],[3,3,1,3,1,2]) == [7,0,8,0,0,6])



