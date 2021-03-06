import matplotlib.pyplot as plt

class postProcess:

	tableCol1Name = '  Item # '
	tableCol2Name = ' Weight (in kg) '
	tableCol3Name = ' Value (in $) '
	tableFiller = ' '
	width = len(tableCol1Name+tableCol2Name+tableCol3Name)+6
	dashes = ''.center(width, '-')

	def __init__(self, solution):

		self.solution = solution

	# function that prints to screen the list of items with their corresponding weights and values
	def printProblemSetupToScreen(self):
		print()
		print('PROBLEM SETUP'.center(postProcess.width, '*'), sep='')
		print(f'Maximum Weight Capacity: {self.solution.maxWeightCapacity} kg'.center(postProcess.width, postProcess.tableFiller), '\n')
		print(postProcess.tableCol1Name, postProcess.tableCol2Name, postProcess.tableCol3Name, sep=' | ')
		print(postProcess.dashes)
		for i in range(self.solution.numberOfItems):
			item = ' ' + f'{i+1}'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
			weight = f'{self.solution.weights[i]}'.center(len(postProcess.tableCol2Name), postProcess.tableFiller)
			value = f'{self.solution.values[i]}'.center(len(postProcess.tableCol3Name), postProcess.tableFiller)
			print(item, weight, value, sep = ' | ')

	# function that prints to screen the knapsack list of items with their corresponding weights and values as well as the total weight and value
	def printProblemSolutionToScreen(self):
		print()
		print('\n','PROBLEM SOLUTION'.center(postProcess.width, '*'), '\n', sep='')
		print(postProcess.tableCol1Name, postProcess.tableCol2Name, postProcess.tableCol3Name, sep=' | ')
		print(postProcess.dashes)

		for i in self.solution.knapsackItemsIndecies:
			item = ' ' + f'{i+1}'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
			weight = f'{self.solution.weights[i]}'.center(len(postProcess.tableCol2Name), postProcess.tableFiller)
			value = f'{self.solution.values[i]}'.center(len(postProcess.tableCol3Name), postProcess.tableFiller)
			print(item, weight, value, sep = ' | ')
		
		totalName = 'TOTAL'.center(len(postProcess.tableCol1Name)-1, postProcess.tableFiller) 
		totalName = ' ' + totalName
		
		totalWeight = str(self.solution.knapsackItems['total']['weight']) + ' ' + f'(max {self.solution.maxWeightCapacity} kg)'
		totalWeight = totalWeight.center(len(postProcess.tableCol2Name), postProcess.tableFiller)
	
		totalValue = str(self.solution.knapsackItems['total']['value'])
		totalValue = totalValue.center(len(postProcess.tableCol3Name), postProcess.tableFiller)
		
		print(postProcess.dashes)
		print(totalName, totalWeight, totalValue, sep=' | ')
		print()

	# function that plots the results of the knapsack problem on a bar graph
	def plotResults(self):
		plt.figure(1,figsize=(12.0,4.0))
		plt.grid(zorder = 0, which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
		
		barWidth = 1
		xloc = [2*i*barWidth for i in range(self.solution.numberOfItems)]

		count = 0
		for i in range(self.solution.numberOfItems):
			if i in self.solution.knapsackItemsIndecies:
				if count == 0:
					plt.bar(xloc[i], self.solution.values[i], width = barWidth, color = '#0c4b33', zorder=2, label = '$Knapsack$ $Items$')
				else:
					plt.bar(xloc[i], self.solution.values[i], width = barWidth, color = '#0c4b33', zorder=2)
				count += 1
			else:
				plt.bar(xloc[i], self.solution.values[i], width = barWidth, color = '#c9f0dd', zorder=2)
		
		offset = 0.03*max(self.solution.values)
		for i in range(self.solution.numberOfItems):
			plt.text(xloc[i], self.solution.values[i]+offset, f'{self.solution.values[i]}\$/{self.solution.weights[i]}kg', ha = 'center', va = 'center', fontsize = 6)

		plt.xticks(xloc, [f'{i+1}' for i in range(self.solution.numberOfItems)], rotation = 0)
		plt.legend(loc = 'best')
		plt.ylim([0 , max(self.solution.values) + int(0.25*max(self.solution.values)) ])
		plt.xlabel('$Items$')
		plt.ylabel('$Value$ $(in$ $\$)$')
		plt.title(f"$0/1$ $Knapsack$ $Solution$ $\\rightarrow$ $Total$ $Weight$ $=$ {self.solution.knapsackItems['total']['weight']}$kg$ $(max$ {self.solution.maxWeightCapacity}$kg)$, $Value$ $=$ {self.solution.knapsackItems['total']['value']}\$")
		plt.savefig('01knapsackSolution.png', bbox_inches='tight', dpi = 250)