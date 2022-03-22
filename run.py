

import numpy as np

from parameterCheck import parameterCheck

#----------USER-DEFINED-PARAMETERS----------#
maxWeightCapacity = 7 # in kilograms, must be integer
numberOfItems = 5 # number of items --> the size of the weights/values arrays defined below must be equal to the numberOfItems variable

generationMethod = 'random' # 'manual' or 'random' --> specifices how the weights/values of the knapsack problem are generated
randomItemWeightLimit = 7
randomItemValueLimit = 100 

# If generationMethod == 'manual', define weights/values below
manualWeights = np.array([3,1,3,4,2], dtype = np.int32) # in kilograms
manualValues = np.array([2,2,4,5,3], dtype = np.int32) # in dollars


if generationMethod == 'manual':
	parameterCheck(numberOfItems, maxWeightCapacity, weights = manualWeights, values = manualValues)
	#solve = knapsackAlgorithm(numberOfItems, maxWeightCapacity, weights, values)
elif generationMethod == 'random':
	parameterCheck(numberOfItems, maxWeightCapacity)
	randomWeights = np.array([np.random.randint(1, randomItemWeightLimit) for i in range(numberOfItems)], dtype = np.int32)
	randomValues = np.array([np.random.randint(1, randomItemValueLimit) for i in range(numberOfItems)], dtype = np.int32)
	print(randomWeights, randomValues)
	#solve = knapsackAlgorithm(numberOfItems, maxWeightCapacity, weights, values)
else:
	pass


