from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import pandas as pd


class Kmeans():
    K = 0

    def __init__(self, K):
        self.K = K


    def kmeans_init_centers(self):
        #return a any array witg the same shape like this
        return np.array([[30, -60], [40, -10], [20, 10], [-20, 40]])


    def kmeans_assign_labels(self, X, centers):
        # calculate pairwise distances from data and centers
        D = cdist(X, centers)
        # return index of the closest center
        return np.argmin(D, axis = 1)


    def kmeans_update_centers(self, X, labels, K):
        centers = np.zeros((K, X.shape[1]))
        for k in range(K):
            # collect all points assigned to the k-th cluster
            Xk = X[labels == k, :]
            # take average
            centers[k,:] = np.mean(Xk, axis = 0)
        return centers


    def has_converged(self, centers, new_centers):
        # return True if two sets of centers are the same
        return (set([tuple(a) for a in centers]) ==
            set([tuple(a) for a in new_centers]))


    def kmeans(self, X):
        centers = [self.kmeans_init_centers()]
        labels = []
        it = 0
        while True:
            labels.append(self.kmeans_assign_labels(X, centers[-1]))
            new_centers = self.kmeans_update_centers(X, labels[-1], self.K)
            if self.has_converged(centers[-1], new_centers):
                break
            centers.append(new_centers)
            it += 1
        return (centers, labels, it)


    def kmeans_display(self, X, label):
        (centers, labels, it) = k_means.kmeans(X)
        center = centers[-1]

        X0 = X[label == 0, :]
        X1 = X[label == 1, :]
        X2 = X[label == 2, :]
        X3 = X[label == 3, :]

        plt.scatter(center[0, 0], center[0, 1], marker='s', color= 'b')
        plt.scatter(center[1, 0], center[1, 1], marker='s', color= 'g')
        plt.scatter(center[2, 0], center[2, 1], marker='s', color= 'r')
        plt.scatter(center[3, 0], center[3, 1], marker='s', color= 'y')

        plt.plot(X0[:, 0], X0[:, 1], 'bo', markersize=4, alpha=.8)
        plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=4, alpha=.8)
        plt.plot(X2[:, 0], X2[:, 1], 'ro', markersize=4, alpha=.8)
        plt.plot(X3[:, 0], X3[:, 1], 'yo', markersize=4, alpha=.8)

        plt.axis('equal')
        plt.plot()
        plt.show()


if __name__ == '__main__':
    #initialize Kmeans object with 4 clusters
    k_means = Kmeans(4)

    #Load dataframe and convert to np.array
    X = np.array(pd.read_csv('position.csv'))

    #Apply k_means algorithms
    (centers, labels, it) = k_means.kmeans(X)

    # Show 4 final centers
    print('Centers found by algorithm:')
    print(centers[-1])

    #Visualize on chart
    k_means.kmeans_display(X, labels[-1])