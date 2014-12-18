'''
Created on Dec 7, 2014

@author: Shahar Weinstock
'''
import numpy as np

def HMM(data,order=3):
    m = data.shape[0]
    n = data.shape[1]
    elements = int(max(np.unique(data))+1)
    models = []
    for i in xrange(m):
        print i
        matrix = np.zeros((elements**order,elements))
        for j in xrange(n-order):
            matrix[data[i,j]*elements**2+data[i,j+1]*elements+data[i,j+2],data[i,j+order]] += 1
        for k in xrange(elements**order):
            total = sum(matrix[k,:]) + 1
            matrix[k,:] =  (matrix[k,:] + 1.0/elements)/total
        models.append(matrix) 
    np.save('C:\Users\user\workspace\\3HMM_Sunday', models)  # @UndefinedVariable