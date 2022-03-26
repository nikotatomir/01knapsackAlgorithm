

class postProcess:

	tableCol1Name = '  Item # '
	tableCol2Name = ' Weight (in kg) '
	tableCol3Name = ' Value (in $) '
	tableFiller = ' '
	width = len(tableCol1Name+tableCol2Name+tableCol3Name)+6
	dashes = ''.center(width, '-')

	def __init__(self, solution):

		self.solution = solution

	def printProblemSetupToScreen(self):
		print()
		print('PROBLEM SETUP'.center(postProcess.width, '*'), sep='')
		print(f'Maximum Weight Capacity: {self.solution.maxWeightCapacity} kg'.center(postProcess.width, postProcess.tableFiller), '\n')
		print(postProcess.tableCol1Name, postProcess.tableCol2Name, postProcess.tableCol3Name, sep=' | ')
		print(postProcess.dashes)
		for i in range(self.solution.numberOfItems):
			item = ' ' + f'{i}'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
			weight = f'{self.solution.weights[i]}'.center(len(postProcess.tableCol2Name), postProcess.tableFiller)
			value = f'{self.solution.values[i]}'.center(len(postProcess.tableCol3Name), postProcess.tableFiller)
			print(item, weight, value, sep = ' | ')

	def printProblemSolutionToScreen(self):
		print()
		print('\n','PROBLEM SOLUTION'.center(postProcess.width, '*'), '\n', sep='')
		print(postProcess.tableCol1Name, postProcess.tableCol2Name, postProcess.tableCol3Name, sep=' | ')
		print(postProcess.dashes)
		chosenItems = self.solution.getKnapsackItemsIndecies()
		totalWeight, totalValue = 0, 0
		for i in chosenItems:
			item = ' ' + f'{i}'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
			weight = f'{self.solution.weights[i]}'.center(len(postProcess.tableCol2Name), postProcess.tableFiller)
			value = f'{self.solution.values[i]}'.center(len(postProcess.tableCol3Name), postProcess.tableFiller)
			print(item, weight, value, sep = ' | ')

			totalWeight += self.solution.weights[i]
			totalValue += self.solution.values[i]
		
		totalNameStr = ' ' + 'TOTAL'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
		totalWeightStr = str(totalWeight) + ' ' + f'(max {self.solution.maxWeightCapacity} kg)'
		totalValueStr = str(totalValue).center(len(postProcess.tableCol3Name), postProcess.tableFiller)
		print(postProcess.dashes)
		print(totalNameStr, totalWeightStr.center(len(postProcess.tableCol2Name), postProcess.tableFiller), totalValueStr, sep=' | ')
