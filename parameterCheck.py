

import numpy as np
import sys

class parameterCheck:

	def __init__(self, numberOfItems, maxWeightCapacity, weights = None, values = None):

		self.numberOfItems = numberOfItems
		self.maxWeightCapacity = maxWeightCapacity
		
		self.executeGeneralCheck()

		if weights is None and values is None:
			pass
		else:
			self.executeManualWeightsValuesCheck()
			print(weights)
			print(values)


	# function that checks if numberOfItems and maxWeightCapacity are positive integers
	def executeGeneralCheck(self):
		pass

	# function that checks if the length of the manually created weights and values arrays are equal to numberOfItems variable 
	# also checks if the weight and values arrays are positive integers
	def executeManualWeightsValuesCheck(self):
		pass
