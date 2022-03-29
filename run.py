import numpy as np

from src.parameterCheck import parameterCheck
from src.knapsackAlgorithm import knapsackAlgorithm
from src.postProcess import postProcess

#----------USER-DEFINED-PARAMETERS----------#
maxWeightCapacity = 7 # in kilograms, must be integer
numberOfItems = 5 # number of items --> the size of the weights/values arrays defined below must be equal to the numberOfItems variable

generationMethod = 'manual' # 'manual' or 'random' --> specifices how the weights/values of the knapsack problem are generated

# If generationMethod == 'random', define weights/values upper limits below
randomItemWeightLimit = 7
randomItemValueLimit = 10

# If generationMethod == 'manual', define weights/values below
manualWeights = np.array([3,1,3,4,2], dtype = np.int32) # in kilograms
manualValues = np.array([2,2,4,5,3], dtype = np.int32) # in dollars

#---------------SOLUTION--------------------#
if generationMethod == 'manual':
	# do parameter check to see if all inputs are valid
	parameterCheck(numberOfItems, maxWeightCapacity, weights = manualWeights, values = manualValues)
	# solve knapsack problem
	solution = knapsackAlgorithm(numberOfItems, maxWeightCapacity, manualWeights, manualValues)
elif generationMethod == 'random':
	# do parameter check to see if all inputs are valid
	parameterCheck(numberOfItems, maxWeightCapacity, randomWeightLimit = randomItemWeightLimit, randomValueLimit = randomItemValueLimit)
	# get random weights and values arrays
	randomWeights = np.array([np.random.randint(1, randomItemWeightLimit+1) for i in range(numberOfItems)], dtype = np.int32)
	randomValues = np.array([np.random.randint(1, randomItemValueLimit+1) for i in range(numberOfItems)], dtype = np.int32)
	# solve knapsack problem
	solution = knapsackAlgorithm(numberOfItems, maxWeightCapacity, randomWeights, randomValues)
else:
	pass

#--------------POST-PROCESS-----------------#
# initialize postProcess class
pp = postProcess(solution)
# print to screen the list of possible knapsack items with their corresponding weights and values
pp.printProblemSetupToScreen()
# print to screen the chosen list of knapsack items with their corresponding weights and values as well as the total weight and value of the knapsack
pp.printProblemSolutionToScreen()
# plot the results of the knapsack problem to a bar graph
pp.plotResults()

