import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def load_csv(path):
    return pd.read_csv(path)


def h(w, x):
    '''
    To compute output with input x,w
    '''
    return np.sign(np.dot(w.T, x))


def has_converged(X, y, w):
    '''
    Compare h(w, X) to ground truth y to check whether the algorithm has converged or not
    '''
    return np.array_equal(h(w, X), y)


def perceptron(X, y, w_init):
    w = [w_init]
    N = X.shape[1]
    mis_points = []
    while True:
        for i in range(N):
            xi = X[:, i].reshape(3, 1)
            print(xi)
            yi = y[0, i]
            if h(w[-1], xi)[0] != yi:
                mis_points.append(i)
                w_new = w[-1] + yi * xi
                w.append(w_new)

        if has_converged(X, y, w[-1]):
            break
    return (w, mis_points)


def cut_data(data):
    data1 = []
    data2 = []
    for i in range(data.shape[0]):
        if data[i, 2] == -1:
            data1.append(data[i, :])
        else:
            data2.append(data[i, :])
    data1 = np.array(data1)
    data2 = np.array(data2)

    return data1, data2


def visualize(data, data1, data2, w, mis_points):

    plt.plot(data1[:, 0], data1[:, 1], 'go', markersize=4, alpha=.8)
    plt.plot(data2[:, 0], data2[:, 1], 'yo', markersize=4, alpha=.8)

    for index in mis_points:
        plt.scatter(data[index, 0], data[index, 1], marker='s', color='b')

    def draw_line(w):
        w0, w1, w2 = w[0], w[1], w[2]
        if w2 != 0:
            x11, x12 = -250, 250
            return plt.plot([x11, x12], [-(w1 * x11 + w0) / w2, -(w1 * x12 + w0) / w2], 'k')
        else:
            x10 = -w0 / w1
            return plt.plot([x10, x10], [-250, 250], 'k')

    draw_line(w)
    plt.axis('equal')
    plt.plot()
    plt.show()


if __name__ == '__main__':
    # load data and convert to numpy array
    df = load_csv('PLA.csv')
    data = np.array(df)

    # processing input to satisfy with function's input
    X = np.transpose(data[:, :2])
    y = np.transpose(data[:, 2].reshape(data.shape[0], 1))
    ones = np.ones_like(y)
    Xbar = np.concatenate((ones, X))
    y[y==0] = -1
    print(Xbar.shape, y)
    d = Xbar.shape[0]
    w_init = np.random.randn(d, 1)
    print(w_init)

    #apply PLA algorithms to find seperated line and missed points
    w, mis_points = perceptron(Xbar, y, w_init)
    print(w)
    print(mis_points)
    print(w[-1])
    print(w[-1].shape)
    print(w[-1][0])

    #Visualize line with data points
    data1, data2 = cut_data(data)
    visualize(data, data1, data2, w[-1], mis_points)




