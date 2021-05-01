# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/30 19:58:59 by rgero             #+#    #+#              #
#    Updated: 2021/05/01 14:06:10 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import sys
import ft_function as ft
import matplotlib.pyplot as plt

def ft_mean(l):
    return sum(l) / len(l)

def ft_std(l):
    mean = ft_mean(l)
    diff = 0
    len_l = len(l)
    for i in l:
        diff = diff + (i - mean) ** 2
    return (diff / len_l) ** 0.5

def ft_mserror(x, y, theta):
    l = []
    len_l = len(y)
    for i in range(len_l):
        y_pred = ft.estimatePrice(theta, x[i])
        l.append((y_pred - y[i]) ** 2)
    return ft_mean(l)

def get_value(filename, df, column):
    l_std = []
    l = df[column].tolist()
    mean = ft_mean(l)
    std = ft_std(l)
    for i in l:
         if i < 0:
              print(f'\nError: {column} is negative in the file {filename}')
              exit(1)
         l_std.append((i - mean) / std)
    return l, l_std, mean, std

def get_gradient(theta, learning_rate, x_std, y_std):
    l_0 = []
    l_1 = []
    len_l = len(x_std)
    for i in range(len_l):
         l_0.append(ft.estimatePrice(theta, x_std[i]) - y_std[i])
         l_1.append((ft.estimatePrice(theta, x_std[i]) - y_std[i]) * x_std[i])
    gradient_0 = learning_rate * ft_mean(l_0)
    gradient_1 = learning_rate * ft_mean(l_1)
    return ((gradient_0, gradient_1))

def plot_value(x, y , real_theta, theta):
    fig, axes = plt.subplots(1, 2, figsize = (12,5))
    axes[0].plot(x[0], y[0], 'ro')
    axes[0].set_title('Original values')
    axes[0].set_xlabel('Mileage')
    axes[0].set_ylabel('Price')
    x_min = min(x[0])
    x_max = max(x[0])
    y_min = ft.estimatePrice(real_theta, x_min)
    y_max = ft.estimatePrice(real_theta, x_max)
    axes[0].plot([x_min, x_max], [y_min, y_max])
    axes[1].plot(x[1], y[1], 'ro')
    axes[1].set_title('Standardized values')
    axes[1].set_xlabel('Mileage')
    axes[1].set_ylabel('Price')
    x_std_min = min(x[1])
    x_std_max = max(x[1])
    axes[1].plot([x_std_min, x_std_max], [ft.estimatePrice(theta, x_std_min),\
        ft.estimatePrice(theta, x_std_max)])
    plt.show()

def get_real_theta(theta, mean_x, std_x, mean_y, std_y):
    theta_0 = mean_y + theta[0] * std_y - theta[1] * std_y * mean_x / std_x
    theta_1 = theta[1] * std_y / std_x
    return ((theta_0, theta_1))

def save_real_thetas(filename, real_theta):
    with open(filename, 'w') as f:
        f.write('theta0,theta1\n')
        f.write("%f,%f" %(real_theta[0], real_theta[1]))

def train(arg, filename, columns, learning_rate, number_epoch):
    if path.exists(filename):
        df = ft.ft_read_csv(filename, columns)
        theta = [0.0, 0.0]
        x, x_std, mean_x, std_x = get_value(filename, df, columns[0])
        y, y_std, mean_y, std_y = get_value(filename, df, columns[1])
        i = 0
        if '-err' in arg:
            print('Mean squared error (MSE) after each iteration')
            print('iter : MSE')
        while i < number_epoch:
            gradient = get_gradient(theta, learning_rate, x_std, y_std)
            theta[0] -= gradient[0]
            theta[1] -= gradient[1]
            if '-err' in arg:
                print("{:5d}: {}".format(i + 1, ft_mserror(x_std, y_std, theta)))
            i += 1
    else:
        print(f'\nError: {filename} is missing')
        exit(1)
    real_theta = get_real_theta(theta, mean_x, std_x, mean_y, std_y)
    save_real_thetas('params.csv', real_theta)
    if '-v' in arg:
        plot_value((x, x_std), (y, y_std), real_theta, theta)

def get_arg():
    l = []
    i = 0
    for arg in sys.argv:
        if arg in ('-v', '-err'):
            l.append(arg)
        if arg == '-h':
            ft.print_usage()
            exit(0)
        if i > 0 and arg not in ('-v', '-err', '-h'):
            ft.print_usage()
            exit(0)
        i += 1
    return(l)

if __name__ == "__main__":
    arg = get_arg()
    train(arg, "data.csv", ['km', 'price'], 0.1, 100)