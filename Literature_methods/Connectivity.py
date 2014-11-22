'''
Created on Nov 20, 2014

@author: user
'''
import numpy as np
def Conn(labels,distanceMat):
    not_match = 0.0
    for index,label in enumerate(labels):
        dist = distanceMat[index,:]
        min_val = min(n for n in dist if n>0)
        if label <> labels[list(dist).index(min_val)]:
            not_match += 1
    return (1-not_match/len(labels))