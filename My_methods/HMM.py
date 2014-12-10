'''
Created on Dec 7, 2014

@author: Shahar Weinstock
'''
import numpy as np

def HMM(data,order):
    m = data.shape[0]
    n = data.shape[1]
    elements = int(max(np.unique(data))+1)
    models = []
    for i in xrange(m):
        matrix = np.zeros((elements,elements))
        for j in xrange(n-order):
            matrix[data[i,j],data[i,j+order]] += 1
        for k in xrange(elements):
            total = max([sum(matrix[k,:]),1])
            matrix[k,:] =  matrix[k,:]/total
        models.append(matrix)    
            
    np.save('C:\Users\user\workspace'+str(order)+'//HMM_Sunday', models)  # @UndefinedVariable