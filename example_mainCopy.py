'''
Created on Oct 26, 2014

@author: user
'''
import os, sys, inspect, time  # @UnusedImport
sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
import numpy as np
from sklearn import metrics
from My_methods import Markov, Markov_JS_distMat
from Literature_methods import LCSS_distMat


# name = '\JS_DBSCAN'
# dist_name = '\\3MM_JS_distMat.txt'
models_name = '\same_1MM.npy'
data_name = '\data2.csv'
path = 'C:\Users\user\workspace\Results\New example' 
# if not os.path.exists(path+):os.makedirs(path+name)
 
'''***************Load data***************'''
##################################################################
start = time.time()
print "loading data"
# dist = np.loadtxt(path+dist_name,delimiter = ' ')  # @UndefinedVariable
data = np.loadtxt(path+data_name,delimiter = ',')  # @UndefinedVariable
models = np.load(path+models_name)  # @UndefinedVariable
# Aff = 1-dist
end = time.time()
print "load time is %s seconds " %str(int(end-start))

#===============================================================================
# models = Markov.MM(data, 1)
# np.save(path+'\different_1MM', models)  # @UndefinedVariable
#===============================================================================

dist = Markov_JS_distMat.MM_distMat(models)
np.savetxt(path+'\\same_JS_distMat.csv', dist, delimiter=",")  # @UndefinedVariable

#===============================================================================
# dist = LCSS_distMat.LCSS_distMat(data)
# np.savetxt(path+'\\same_LCSS_distMat.csv', dist, delimiter=",")  # @UndefinedVariable
#===============================================================================
