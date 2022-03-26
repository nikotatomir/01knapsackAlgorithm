

import numpy as np

from parameterCheck import parameterCheck
from knapsackAlgorithm import knapsackAlgorithm
from postProcess import postProcess

#----------USER-DEFINED-PARAMETERS----------#
maxWeightCapacity = 7 # in kilograms, must be integer
numberOfItems = 5 # number of items --> the size of the weights/values arrays defined below must be equal to the numberOfItems variable

generationMethod = 'manual' # 'manual' or 'random' --> specifices how the weights/values of the knapsack problem are generated

# If generationMethod == 'random', define weights/values upper limits below
randomItemWeightLimit = 7
randomItemValueLimit = 100

# If generationMethod == 'manual', define weights/values below
manualWeights = np.array([3,1,3,4,2], dtype = np.int32) # in kilograms
manualValues = np.array([2,2,4,5,3], dtype = np.int32) # in dollars
#-------------------------------------------#

if generationMethod == 'manual':
	# do parameter check to see if all inputs are valid
	parameterCheck(numberOfItems, maxWeightCapacity, weights = manualWeights, values = manualValues)
	# solve knapsack problem
	solution = knapsackAlgorithm(numberOfItems, maxWeightCapacity, manualWeights, manualValues)
elif generationMethod == 'random':
	# do parameter check to see if all inputs are valid
	parameterCheck(numberOfItems, maxWeightCapacity, randomWeightLimit = randomItemWeightLimit, randomValueLimit = randomItemValueLimit)
	# get random weights and values arrays
	randomWeights = np.array([np.random.randint(1, randomItemWeightLimit) for i in range(numberOfItems)], dtype = np.int32)
	randomValues = np.array([np.random.randint(1, randomItemValueLimit) for i in range(numberOfItems)], dtype = np.int32)
	# solve knapsack problem
	solution = knapsackAlgorithm(numberOfItems, maxWeightCapacity, randomWeights, randomValues)
else:
	pass

pp = postProcess(solution)
pp.printProblemSetupToScreen()
pp.printProblemSolutionToScreen()

# chosenItems = solution.getKnapsackItemsIndecies()
# print(chosenItems)
# print('banankgfkfghaa'.center(20, '0'))