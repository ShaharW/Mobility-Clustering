'''
Created on Dec 7, 2014

@author: Shahar Weinstock

Calculating Markov models for sequence data.
Each row is being added with an a-priory constant distribution
(every element in each row is added 1/row_len and being normalized) 
'''
import numpy as np

def HMM(data,order=1):
    m = data.shape[0]
    n = data.shape[1]
    elements = int(max(np.unique(data))+1)
    models = []
    for i in xrange(m):
        print i
        matrix = np.zeros((elements**order,elements))
        for j in xrange(n-order):
            row = sum(data[i,k]*elements**(j+order-k-1) for k in range(j,j+order))
            matrix[row,data[i,j+order]] += 1
        for k in xrange(elements**order):
            total = sum(matrix[k,:]) + 1
            matrix[k,:] =  (matrix[k,:] + 1.0/elements)/total
        models.append(matrix) 
    return models