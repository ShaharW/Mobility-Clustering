'''
Created on Jun 17, 2014

@author: user
'''

def Kmeans(dist,data,k):
    '''***************Imports****************'''
    ##################################################################
    import os, sys, inspect, time  # @UnusedImport
    sys.path.insert(0, 'C:\Users\user\Anaconda\Lib\site-packages')
    
    import matplotlib #@UnresolvedImport @UnusedImport
    from mpl_toolkits.mplot3d import Axes3D  # @UnresolvedImport @UnusedImport
#     import numpy as np
#     import matplotlib.pyplot as plt  # @UnresolvedImport
    from sklearn import cluster, metrics, decomposition  # @UnresolvedImport @UnusedImport
    ##################################################################
    
    '''***************Kmeans***************'''
    ##################################################################

    print "clustering with %d-means" %k
    end = time.time()
    estimator = cluster.KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)    
    labels = estimator.fit(dist).predict(dist)
    ##################################################################
    
    '''***************Clustering evaluation***************
    ##################################################################
    sil_score = metrics.silhouette_score(dist, labels, metric='precomputed')
    
    print 'silhouette score is %s' %str(sil_score)'''
    ##################################################################
    
    end2 = time.time()
    print "model time is %s seconds " %str(int(end2-end))
    
    '''***************present the clusters as 3D data using PCA***************'''
    ##################################################################
    #===========================================================================
    # reduced_data = decomposition.PCA(n_components=3).fit_transform(data)
    # #reduced_data = data
    #  
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # '''Points color'''
    # colors = np.r_[np.linspace(0.1, 1, 5), np.linspace(0.1, 1, 5)]  # @UndefinedVariable
    # mymap = plt.get_cmap("Reds")
    # # get the colors from the color map
    # my_colors = mymap(colors)
    #  
    # ''' Scatter - color by label'''
    # for i in range(reduced_data.shape[0]):
    #     ax.scatter(reduced_data[i,0], reduced_data[i,1], reduced_data[i,2], c=my_colors[labels[i]])
    #  
    # '''
    # for i in range(data.shape[0]):
    #     ax.scatter(data[i,0], data[i,1], data[i,2], c=my_colors[labels[i]])
    # '''
    # plt.show()
    #===========================================================================

    ##################################################################    
    return labels

        
