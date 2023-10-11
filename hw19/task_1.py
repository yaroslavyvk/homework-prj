import numpy as np

zerro_array = np.zeros((4, 3))
print(zerro_array)

ones_array = np.ones((4, 3))
print(ones_array)

numbers_array = np.arange(12).reshape(4, 3)
print(numbers_array)

x_values = np.arange(1, 101)
y_values = 2 * x_values**2 + 5
for x, y in zip(x_values, y_values):
    print(f"x: {x}, F(x): {y}")

x_exp_values = np.arange(-10, 11)
y_exp_values = np.exp(-x_exp_values)
for x_exp, y_exp in zip(x_exp_values, y_exp_values):
    print(f"x_exp: {x_exp}, F(x_exp): {y_exp}")
