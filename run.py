

import numpy as np

#----------USER-DEFINED-PARAMETERS----------#
generationMethod = 'manual' # 'manual' or 'random' --> specifices how the weights/values of the knapsack problem are generated
maxWeightCapacity = 7 # in kilograms, must be integer
# If generationMethod == 'manual', define weights/values below
weights = np.array([3,1,3,4,2], dtype = np.int32) # in kilograms
values = np.array([2,2,4,5,3], dtype = np.int32) # in dollars