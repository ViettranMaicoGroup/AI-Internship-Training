import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_csv(path):
    data_frame = pd.read_csv(path)
    return np.array(data_frame)


def plot(X, y, y_predict):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(X, y, 'bo', X, y_predict, markersize=5)
    plt.show()


def linear_regression(X, y):
    #building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)
    #Calculating weights of the fitting line
    A = np.dot(Xbar.T, Xbar)
    b = np.dot(Xbar.T, y)
    w = np.dot(np.linalg.pinv(A), b).reshape(1, 2)
    return (w[0, 0], w[0, 1])


def train_test_split(data, test_size):
    random.shuffle(data)
    try:
        assert(test_size >= 0 and test_size <= 1)
    except Exception:
        print("Test_size must in [0, 1]")

    train_size = 1 - test_size
    limit = int(np.floor(train_size*data.shape[0]))
    X_train = data[:limit, :-1]
    y_train = data[:limit, -1]
    X_test = data[limit:, :-1]
    y_test = data[limit:, -1]

    return (X_train, y_train, X_test, y_test)


def total_error(real_result, predict_result):
    error = 1/2*(real_result.reshape(-1)- predict_result.reshape(-1))**2
    # error = abs(real_result.reshape(-1) - predict_result.reshape(-1))
    return error.sum()


if __name__ == "__main__":
    random.seed(42)

    #load data
    path = "linear_regression.csv"
    data  = load_csv(path)
    print(data.shape)

    #train test split
    X_train, y_train, X_test, y_test = train_test_split(data, 0.8)
    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

    #Using linear regression to predict output
    w_0, w_1 = linear_regression(X_train, y_train)
    y_test_predict = np.array(list(map(lambda var : var*w_1 + w_0, X_test)))
    print(y_test_predict)

    #Calculate total of errors
    print(total_error(y_test, y_test_predict))

    #Visualine data and predict line
    plot(X_test, y_test, y_test_predict)