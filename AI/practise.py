import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.animation as animation


def cost(x):
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(x) - b, 2)**2


def grad(x):
    m = A.shape[0]
    return 1/m * A.T.dot(A.dot(x)-b)


def gradient_descent(x_init, learning_rate, iteration):
    x_list = [x_init]

    for i in range(iteration):
        x_new = x_list[-1] - learning_rate*grad(x_list[-1])
        if np.linalg.norm(grad(x_new)) / len(x_new) < 0.0001:  # when to stop GD
            break
        x_list.append(x_new)

    return x_list


# Data
A = np.array([[2, 9, 7, 9, 11, 16, 25, 23, 22, 29, 29, 35, 37, 40, 46]]).T
b = np.array([[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]).T

plt.plot(A, b, 'ro')

lr = linear_model.LinearRegression()
x0_gd = np.linspace(1, 46, 100).reshape(-1, 1)
lr.fit(A, b)
y0_gd = lr.predict(x0_gd)
plt.plot(x0_gd, y0_gd)


plt.show()
