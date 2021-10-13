import numpy as np
import matplotlib.pyplot as plt


def plot_line_chart(X, Y):
    plt.figure(num= 3, figsize=(8, 5))
    plt.title("ABC")
    plt.plot(X, Y,
             color= 'red',
             linewidth= 2.0,
             linestyle= '-'
             )
    plt.xlabel("Hoành độ")
    plt.ylabel("Tung độ")
    plt.show()


def plot_bar_chart(X, Y):
    fig, ax = plt.subplots()
    index = np.arange(len(X))
    bar_width = 0.35
    opacity = 0.8
    plt.bar(index, X, bar_width,
                     alpha= opacity,
                     color= 'g',
                     label= '1')

    plt.bar(index + bar_width, Y, bar_width,
                     alpha= opacity,
                     color= 'y',
                     label= '2')

    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.title('ABC')
    plt.xticks(index + bar_width, index + 1)
    plt.legend()
    plt.tight_layout()
    plt.show()


def subplot(MATRIX_1, MATRIX_2, MATRIX_3, MATRIX_4):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle("ABC")
    axs[0,0].plot(MATRIX_1[0,:], MATRIX_1[1,:], color= 'g')
    axs[0,0].set_title("abc1")
    axs[0,1].plot(MATRIX_2[0,:], MATRIX_2[1,:], color= 'r')
    axs[0,1].set_title("abc2")
    axs[0, 1].plot(MATRIX_3[0, :], MATRIX_3[1, :], color= 'y')
    axs[1,0].set_title("abc3")
    axs[1,1].plot(MATRIX_4[0,:], MATRIX_4[1,:], color= 'y')
    axs[1,1].set_title("abc4")
    for ax in axs.flat:
        ax.set(xlabel= 'x-label', ylabel= 'y-label')
    for ax in axs.flat:
        ax.label_outer()
    plt.show()


if __name__ == "__main__":
    #a
    X = np.array([1, 2, 3, 4])
    Y = np.array([1, 4, 3, 9])
    plot_line_chart(X, Y)
    #b
    XX = np.array([50, 100, 200, 10])
    YY = np.array([90, 30, 25, 50])
    plot_bar_chart(XX, YY)
    #c
    MATRIX_1 = np.array([[1, 2, 3, 4],
                        [0.5, 4, 3, 10]])
    MATRIX_2 = np.array([[1, 2, 3, 4, 5],
                        [0.5, 6, 2, 3, 10]])
    MATRIX_3 = np.array([[],[]])
    MATRIX_4 = np.array([[1, 2, 4],
                        [0.5, 5, 0.5]])
    #visualize in suplot
    subplot(MATRIX_1, MATRIX_2, MATRIX_3, MATRIX_4)