
import numpy as np

class knapsackAlgorithm():

	def __init__(self, numberOfItems, maxWeightCapacity, weights, values):

		self.numberOfItems = numberOfItems
		self.maxWeightCapacity = maxWeightCapacity
		self.weights = weights
		self.values = values

	# function that constructs the valueMatrix based on the item weights & values
	def getValueMatrix(self):
		valueMatrix = np.zeros((self.numberOfItems + 1 , self.maxWeightCapacity + 1), dtype = np.int32)
		for i in range(1, self.numberOfItems + 1):
			for j in range(self.maxWeightCapacity + 1):
				if j < self.weights[i-1]:
					valueMatrix[i,j] = valueMatrix[i-1,j]
				else:
					valueMatrix[i,j] = max(valueMatrix[i-1,j], self.values[i-1]+valueMatrix[i-1,j-self.weights[i-1]])

		return valueMatrix

	# function that extracts the items that provide the maximum total value given the knapsack maximum weight capacity
	def getKnapsackItemsIndecies(self):
		valueMatrix = self.getValueMatrix()
		knapsackItemsIndecies = []
		columnIndex = -1
		for i in reversed(range(1, self.numberOfItems + 1)):
			if valueMatrix[i, columnIndex] == valueMatrix[i-1, columnIndex]:
				continue
			else:
				knapsackItemsIndecies.append(i-1)
				columnIndex -= self.weights[i-1]

			knapsackItemsIndecies.sort()

		return knapsackItemsIndecies


