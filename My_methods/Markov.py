'''
Created on Dec 7, 2014

@author: Shahar Weinstock

Calculating Markov models for sequence data.
Each row of zeros is being added with an a-priory constant distribution-
every element in each row is 1/(size of the row)

The last column is saved for marginal probability of the rows
'''
import numpy as np

def MM(data,order=1):
    m = data.shape[0]
    n = data.shape[1]
    elements = int(max(np.unique(data))+1)
    models = []
    for i in xrange(m):
        print i
        matrix = np.zeros((elements**order,elements+1))
        for j in xrange(n-order):
            row = sum(data[i,k]*elements**(j+order-k-1) for k in range(j,j+order))
            matrix[row,data[i,j+order]] += 1
        for k in xrange(elements**order):
            matrix[k,elements] = sum(matrix[k,0:elements]) # sum every row to the last column
            if matrix[k,elements] == 0:
                matrix[k,0:elements] = [1.0/elements] * elements
            else:
                matrix[k,0:elements] = matrix[k,0:elements]/matrix[k,elements] # normalize each row with 0.01 a-priory
        matrix[:,elements] = matrix[:,elements]/sum(matrix[:,elements])
        models.append(matrix) 
    return models
