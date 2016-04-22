##################################
# Akshat Agrawal and Joseph Hostyk
# CS 124
# Programming Assignment 3
# 4/25/16
#
# kk.py: main functions
##################################

from random import randint
import math
import time
import csv
import standard
import prepartition


maxIter = 5 # should be 25000 in final testing
PREPARTITION = 0
RANDMOVE = 1

def createRandNumFiles():
	for i in range(50):
		f = open("50randNums{}.txt".format(i), "w")
		for i in range (0, 101):
			f.write(str(randint(0,math.pow(10, 12)))+"\n")
		f.close()
	return

# Karmarkar-Karp. Takes in the name of a file with nums.
# Output: residue
def kk(ns):
	t0 = time.time()
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
	return (nums[0], time.time()-t0)


def simulations():
	with open('results.csv','w') as csvfile:
		for i in range(50):
			print "Round {}:".format(i)
			f = open("50randNums{}.txt".format(i), "r")
			nums = [int(a) for a in f]
			f.close()

			fieldnames = ["filenum", "kk", "time kk", "std rand", "time srand", "std hill", "time shill", "std simAnneal", "time sanneal", "part rand", "time prand", "part hill", "time phill", "part simAnneal", "time psim"]
			csvwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)
			#csvwriter.writeheader()
			kkres, tkk = kk(nums)
			sRR, tsrr = standard.repeatedRandom(nums)
			sHC, tshc = standard.hillClimbing(nums)
			sSA, tssa = standard.simulAnnealing(nums)
			pRR, tprr = prepartition.repeatedRandom(nums)
			pHC, tphc = prepartition.hillClimbing(nums)
			pSA, tpsa = prepartition.simulAnnealing(nums)
			print "#{}: kk: {}, tkk: {}, sHC: {}, tshc: {}, sSA: {}, tssa: {}, pRR: {}, tprr: {}, pHC: {}, tphc: {}, pSA: {}, tpsa: {}".format(i, kkres, tkk, sHC, tshc, sSA, tssa, pRR, tprr, pHC, tphc, pSA, tpsa)
			csvwriter.writerow({"filenum": i, "kk": kkres, "time kk": tkk, "std rand": sRR, "time srand": tsrr, "std hill": sHC, "time shill": tshc, "std simAnneal": sSA, "time sanneal": tssa, "part rand": pRR, "time prand": tprr, "part hill": pHC, "time phill": tphc, "part simAnneal": pSA, "time psim": tpsa})




if __name__ == '__main__':
	simulations()

	# f = open("50randNums.txt", "r")
	# nums = [int(a) for a in f]
	# f.close()
	#csvwriter.writerow({"kk": kk(nums),"part rand": , "part hill": .hillClimbing(nums), "part simAnneal":.(nums)})
	# print kk(nums)
	# print standard.repeatedRandom(nums)
	# print standard.hillClimbing(nums)
	# print standard.simulAnnealing(nums)
	# print prepartition.repeatedRandom(nums)
	# print prepartition.hillClimbing(nums)
	# print prepartition.simulAnnealing(nums)

	# #kk("testNums.txt")
	# #kk("50randNums.txt")
	# prepartition([10,8,7,6,5])


