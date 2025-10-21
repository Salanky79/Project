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
        if np.linalg.norm(grad(x_new)) < 0.0001:  # when to stop GD
            break
        x_list.append(x_new)

    return x_list


# Data
b = np.array([[2, 5, 7, 9, 11, 16, 19, 23, 22, 29, 29, 35, 37,
             40, 46, 42, 39, 31, 30, 28, 20, 15, 10, 6]]).T
A = np.array([[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]).T

# Draw data
fig1 = plt.figure("GD for Linear Regression")
ax = plt.axes(xlim=(-10, 50), ylim=(-10, 50))
plt.plot(A, b, 'ro')

# Thêm cột bình phương và cột 1

x_square = A**2
ones = np.ones_like(A)
A = np.concatenate((ones, A, x_square), axis=1)

# Huấn luyện mô hình
lr = linear_model.LinearRegression()
lr.fit(A, b)

x0_gd = np.linspace(1, 46, 10000).reshape(-1, 1)
x0_full = np.concatenate((np.ones_like(x0_gd), x0_gd, x0_gd**2), axis=1)
y0_gd = lr.predict(x0_full)
plt.plot(x0_gd, y0_gd, color='green')


x_init = np.array([[-2.1],
                   [5.1],
                   [-2.1]])

y0_init = x_init[0][0] + x_init[1][0]*x0_gd + x_init[2][0]*x0_gd*x0_gd
plt.plot(x0_gd, y0_init, color="black")

# Run gradient descent
iteration = 70
learning_rate = 0.000001

x_list = gradient_descent(x_init, learning_rate, iteration)

# plot black x_list
for i in range(len(x_list)):
    y0_x_list = x_list[i][0] + x_list[i][1]*x0_gd + x_list[i][2]*x0_gd*x0_gd
    plt.plot(x0_gd, y0_x_list, color='black', alpha=0.3)

# Draw animation
line, = ax.plot([], [], color="blue")


def update(i):
    y0_gd = x_list[i][0][0] + x_list[i][1][0] * \
        x0_gd + x_list[i][2][0]*x0_gd*x0_gd
    line.set_data(x0_gd, y0_gd)
    return line,


iters = np.arange(1, len(x_list), 1)
line_ani = animation.FuncAnimation(fig1, update, iters, interval=50, blit=True)

# legend for plot
plt.legend(('Value in each GD iteration', 'Solution by formular',
           'Inital value for GD'), loc=(0.52, 0.01))
ltext = plt.gca().get_legend().get_texts()

# title
plt.title("Gradient Descent Animation")

plt.show()
