import numpy as np

class knapsackAlgorithm():

	def __init__(self, numberOfItems, maxWeightCapacity, weights, values):

		self.numberOfItems = numberOfItems
		self.maxWeightCapacity = maxWeightCapacity
		self.weights = weights
		self.values = values

		self.valueMatrix = self.getValueMatrix()
		self.knapsackItemsIndecies = self.getKnapsackItemsIndecies()
		self.knapsackItems = self.getKnapsackItems()

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

	# function that extracts the items indecies that provide the maximum total value given the knapsack maximum weight capacity
	def getKnapsackItemsIndecies(self):
		knapsackItemsIndecies = []
		columnIndex = -1
		for i in reversed(range(1, self.numberOfItems + 1)):
			if self.valueMatrix[i, columnIndex] == self.valueMatrix[i-1, columnIndex]:
				continue
			else:
				knapsackItemsIndecies.append(i-1)
				columnIndex -= self.weights[i-1]

			knapsackItemsIndecies.sort()

		return knapsackItemsIndecies

	# function that returns a dictionary of the knapsack items, weights and values as well as the total weight and value
	def getKnapsackItems(self):
		knapsackItems = {}
		totalWeight, totalValue = 0, 0
		for i in self.knapsackItemsIndecies:
			itemNo = f'item {i+1}'
			knapsackItems[itemNo] = {}
			knapsackItems[itemNo]['weight'] = self.weights[i]
			knapsackItems[itemNo]['value'] = self.values[i]

			totalWeight += self.weights[i]
			totalValue += self.values[i] 

		knapsackItems['total'] = {}
		knapsackItems['total']['weight'] = totalWeight
		knapsackItems['total']['value'] = totalValue

		return knapsackItems


