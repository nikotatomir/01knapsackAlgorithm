

import numpy as np
import sys

class parameterCheck:

	def __init__(self, numberOfItems, maxWeightCapacity, randomWeightLimit = None, randomValueLimit = None, weights = None, values = None):

		self.__numberOfItems = numberOfItems
		self.__maxWeightCapacity = maxWeightCapacity
		
		self.__randomWeightLimit = randomWeightLimit
		self.__randomValueLimit = randomValueLimit

		self.__weights = weights
		self.__values = values

		self.generalCheck()

		if self.__weights is None and self.__values is None and self.__randomWeightLimit is None and self.__randomValueLimit is None:
			pass
		elif self.__randomWeightLimit is not None and self.__randomValueLimit is not None and self.__weights is None and self.__values is None: 
			# random problem setup
			self.checkRandomArrayWeightValueLimit()
		elif self.__weights is not None and self.__values is not None and self.__randomWeightLimit is None and self.__randomValueLimit is None: 
			# manual problem setup
			self.checkManualArrayLength()
			self.checkManualArrayForPositiveIntegers()
		else:
			pass

	# function that checks if numberOfItems and maxWeightCapacity are positive integers
	def generalCheck(self):
		if self.__numberOfItems <= 0 or not isinstance(self.__numberOfItems, int):
			sys.exit("\n***EXITING PROGRAM***\nError Message: numberOfItems must be a positive nonzero integer")
		elif self.__maxWeightCapacity <= 0 or not isinstance(self.__maxWeightCapacity, int):
			sys.exit("\n***EXITING PROGRAM***\nError Message: maxWeightCapacity must be a positive nonzero integer")
		else:
			pass

	# function that checks if the length of the manually created weights and values arrays are equal to numberOfItems variable 
	def checkManualArrayLength(self):
		if len(self.__weights) != self.__numberOfItems or len(self.__values) != self.__numberOfItems:
			sys.exit("\n***EXITING PROGRAM***\nError Message: The length of the weights and values arrays must be equal to the numberOfItems")
		else:
			pass
	
	# function that checks if weights and values arrays are all positive integers
	def checkManualArrayForPositiveIntegers(self):
		if np.any(self.__weights <= 0) or np.any(self.__values <= 0):
			sys.exit("\n***EXITING PROGRAM***\nError Message: The weights and values arrays must be positive nonzero integers")
		else:
			pass

	# function that checks if the upper limits for the randomly created weight and value arrays are positive nonzero integers greater than 1
	def checkRandomArrayWeightValueLimit(self):
		if self.__randomWeightLimit <= 1 or not isinstance(self.__randomWeightLimit, int):
			sys.exit("\n***EXITING PROGRAM***\nError Message: randomItemWeightLimit must be a positive nonzero integer greater than 1")
		elif self.__randomValueLimit <= 1 or not isinstance(self.__randomValueLimit, int):
			sys.exit("\n***EXITING PROGRAM***\nError Message: randomItemValueLimit must be a positive nonzero integer greater than 1")
		else:
			pass 