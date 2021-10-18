import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels


def load_csv(file_path):
    return pd.read_csv(file_path)


def build_Xbar(X, y):
    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)
    print(Xbar.shape, y.shape)
    return Xbar, y


def grad(Xbar, y, w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T @ (Xbar @ w - y)


def has_converged(X_bar, y, w):
    return np.linalg.norm(grad(X_bar, y, w))/len(w) < 1e-3


def GD_momentum(w_init, X_bar, y, eta, gamma):
    w = np.array(w_init)
    v_old = np.zeros_like(w_init)
    for i in range(100000):
        v_new = gamma * v_old + eta * grad(X_bar, y, w)
        w_new = w - v_new
        if has_converged(X_bar, y, w_new):
            break
        v_old = v_new
        w = w_new
    return w_new[0, 0], w_new[1, 0], i


def visualize(X_test, y_test, y_pred):
    plt.plot(X_test, y_test, "bo", X_test, y_pred, "r-")
    plt.title("Plot from algorithm GD momentum")
    plt.show()
    #Using seaborn
    sns.set_theme(color_codes=True)
    df_test = pd.DataFrame({"Marketing": X_test, "Sales": y_test})
    sns.regplot(x="Marketing", y="Sales", data=df_test, logistic=False, n_boot=500, y_jitter=.03).set_title(
        "Plot with seaborns" )
    plt.show()


if __name__ == "__main__":
    #load dataframe
    df = load_csv("financial.csv")
    X_train, X_test, y_train, y_test = train_test_split(np.array(
        df["Marketing"]), np.array(df["Sales"]), test_size=0.2, random_state=42)

    #convert for valid input to build Xbar function
    X_train = X_train.reshape(len(X_train), 1)
    y_train = y_train.reshape(len(y_train), 1)
    Xbar, y = build_Xbar(X_train, y_train)

    #Initizlize w, assign eta and gamma values and apply gradient momentum to find valid straight line
    w_init = [[2], [1]]
    eta = 0.00001
    gamma = 0.9
    w_0, w_1, i = GD_momentum(w_init, Xbar, y, eta, gamma)
    print(w_0, w_1)

    # Show out real values and predict values to evaluate algorithms easily
    y_test_predict = np.array(list(map(lambda var: var * w_1 + w_0, X_test)))
    print("Real: \n", y_test.reshape(-1))
    print("Predict: \n", y_test_predict.reshape(-1))

    #View out the shape and convert to 1-demension to use in visualize() function
    print(X_test.shape, y_test.shape, y_test_predict.shape)
    X_test = X_test.reshape(-1)
    y_pred = y_test_predict.reshape(-1)
    print(X_test.shape)
    visualize(X_test, y_test, y_pred)
    # print(w_0)