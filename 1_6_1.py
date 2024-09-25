import numpy as np

x_test = [(5, -3), (-3, 8), (3, 6), (0, 0), (5, 3), (-3, -1), (-3, 3)]

w = [-33/13, 9/13, 1] # коеффициенты разделяющей прямой y = kx + b
predict = []
for i in range(len(x_test)):
    predict.append([1 if (w[0] + w[1]*x_test[i][0] +  w[2]*x_test[i][1]) > 0 else -1][0]) # {1; -1} в зависимости от знака скалярного произведения

print(predict)