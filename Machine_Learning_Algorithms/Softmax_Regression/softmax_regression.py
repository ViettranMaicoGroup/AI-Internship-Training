import math
from scipy import sparse
import numpy as np
import pandas as pd



def load_csv(path):
    return pd.read_csv(path)


def convert_labels(y, C):
    '''
    y: labels input
    C: number of class
    Convert to one-hot coding matrix
    '''
    Y = sparse.coo_matrix((np.ones_like(y),(y, np.arange(len(y)))), shape = (C, len(y))).toarray()
    return Y


def softmax(Z):
    e_Z = np.exp(Z - np.max(Z, axis= 0, keepdims= True))
    A = e_Z / e_Z.sum(axis = 0)
    return A


def softmax_regression(X, y, W_init, eta, tol, max_count):
    X = np.transpose(X)
    # y = np.transpose(y)
    W = [W_init]
    C = W_init.shape[1] #number of class
    Y = convert_labels(y, C) #one-hot coding matrix
    N = X.shape[1] #number of training samples
    d = X.shape[0] #data demension

    count = 0
    check_w_after = 20

    while count < max_count:
        for i in range(N):
            xi = X[:, i].reshape(d, 1)
            yi = Y[:, i].reshape(C, 1)
            ai  = softmax(np.dot(W[-1].T, xi))
            W_new = W[-1] + eta*xi.dot((yi - ai).T)
            count += 1

            #has convereged
            if count % check_w_after == 0:
                if np.linalg.norm(W_new - W[-check_w_after]) < tol:
                    return W
            W.append(W_new)
        return W


def predict(W, X):
    X = np.transpose(X)
    A = softmax(W.T.dot(X))
    return np.argmax(A, axis=0)



if __name__ == '__main__':
    np.random.seed(42)
    #Load data and divde into input_data and labels
    df = load_csv('commodity.csv')
    data = np.array(df)
    print(data.shape)
    X = data[:, :-1]
    y = data[:, -1]
    print(y)

    #Initilize learning rate and data to satisfy with input of  algorithm functions
    d = X.shape[1]
    C = 4
    W_init = np.random.randn(d, C)
    print(W_init)
    print(W_init.shape)
    eta = 0.05
    tol = math.e - 4
    max_count = 10000

    #Apply Sofmax Regression algorithm
    W = softmax_regression(X, y, W_init, eta, tol, max_count)
    w = W[-1]
    print(w)
    print(f'W shape: {w.shape}')
    print(f'X shape: {X.shape}')
    print(X[0, :])
    print(predict(w, X[0, : ]))
    Zs = []
    for i in range(X.shape[0]):
        Z = predict(w, X[i][:])
        Zs.append(Z)
    print(Zs)
    print(np.array(Zs).shape)
    print(y.shape)
    Zs = np.array(Zs)
    num = 0
    for i in range(510):
        if y[i] == Zs[i]:
            num += 1
    print(f"Acc: {1.0*num/510}")
