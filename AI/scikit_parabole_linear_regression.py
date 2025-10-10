import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Data
A = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
     15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
b = [2, 5, 7, 9, 11, 16, 19, 23, 22, 29, 29, 35,
     37, 40, 46, 42, 39, 31, 30, 28, 20, 15, 10, 6]

plt.plot(A, b, 'ro')

# Chuẩn bị dữ liệu huấn luyện
A = np.array([A]).T
b = np.array([b]).T

# Thêm cột bình phương và cột 1
x_square = A**2

A_full = np.concatenate((x_square, A), axis=1)

# Huấn luyện mô hình
lr = linear_model.LinearRegression()
lr.fit(A_full, b)

# Dữ liệu test để vẽ
x0 = np.linspace(A.min(), A.max(), 200).reshape(-1, 1)
x0_full = np.concatenate((x0**2, x0), axis=1)
y0 = lr.predict(x0_full)

# Vẽ kết quả
plt.plot(x0, y0, 'b-')
plt.show()
