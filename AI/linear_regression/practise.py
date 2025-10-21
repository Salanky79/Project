import pandas as pd
from sklearn import linear_model

# Dữ liệu gốc
df = pd.read_csv("Final_data.csv")

# Biến số
A = df[['Age', 'Weight (kg)', 'Height (m)', 'Max_BPM',
        'Avg_BPM', 'Session_Duration (hours)']]

# Biến phân loại
workout_dummies = pd.get_dummies(df['Workout_Type'])  # one-hot encoding
A = pd.concat([A, workout_dummies], axis=1)

b = df[['Calories_Burned']]

# Hồi quy tuyến tính nhiều biến
lr = linear_model.LinearRegression()
lr.fit(A, b)

# Dữ liệu mới cần dự đoán
x_test = pd.DataFrame({
    'Age': [25, 30, 28, 35],
    'Weight (kg)': [70, 80, 65, 75],
    'Height (m)': [1.75, 1.8, 1.7, 1.78],
    'Max_BPM': [180, 175, 190, 170],
    'Avg_BPM': [120, 130, 125, 110],
    'Session_Duration (hours)': [1, 1.5, 0.75, 2],
    'Workout_Type': ['Strength', 'HIIT', 'Cardio', 'Yoga']
})

# One-hot encoding dữ liệu mới
x_test_dummies = pd.get_dummies(x_test['Workout_Type'])
for col in workout_dummies.columns:
    if col not in x_test_dummies:
        x_test_dummies[col] = 0

x_test_encoded = pd.concat([x_test.drop('Workout_Type', axis=1),
                            x_test_dummies[workout_dummies.columns]], axis=1)

# Dự đoán
y_pred = lr.predict(x_test_encoded).flatten()  # flatten để thành mảng 1D

# Nối dữ liệu đầu vào với kết quả dự đoán
result = x_test.copy()
result['Predicted_Calories_Burned'] = y_pred

print(result)
