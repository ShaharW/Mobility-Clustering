'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics
from Clustering_methods import Kmedoids
from My_methods import Markov, Markov_JS_distMat
from Literature_methods import LCSS_distMat


# name = '\JS_DBSCAN'
# dist_name = '\\3MM_JS_distMat.txt'
models_name = '\same_1MM.npy'
data_name = '\example data-indel.csv'
path = 'C:\Users\user\workspace\Results\Example' 
# if not os.path.exists(path+):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
start = time.time()
print "loading data"
# dist = np.loadtxt(path+dist_name,delimiter = ' ')  # @UndefinedVariable
data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
# models = np.load(path+models_name)  # @UndefinedVariable

end = time.time()
print "load time is %s seconds " %str(int(end-start))

analysis_name = '\\indel'

####################################################################
models = np.asarray(Markov.MM(data, 1))
dist = Markov_JS_distMat.MM_distMat(models)
np.savetxt(path+analysis_name+'_Markov.csv', dist, fmt='%.2f', delimiter=",")  # @UndefinedVariable
####################################################################
dist = LCSS_distMat.LCSS_distMat(data)
np.savetxt(path+analysis_name+'_LCSS.csv', dist, fmt='%.2f', delimiter=",")  # @UndefinedVariable