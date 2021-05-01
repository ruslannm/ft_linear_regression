# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/29 20:15:26 by rgero             #+#    #+#              #
#    Updated: 2021/05/01 14:19:05 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import ft_function as ft

def predict(filename, columns):
    user_input = input('Please enter a mileage: ')
    if ft.ft_is_number(user_input, 1, 'mileage'):
        mileage = float(user_input)
    else:
        exit(1)
    theta = (0, 0)
    if path.exists(filename):
        df = ft.ft_read_csv(filename, columns)
        theta = (df.iloc[0][columns[0]], df.iloc[0][columns[1]])
    estimate_price = ft.estimatePrice(theta, mileage)
    if estimate_price >= 0:
        print(f'This car costs {round(estimate_price)}.')
    else:
        print('This car doesn\'t cost anything'\
              ' because it has a lot of mileage.')

if __name__ == "__main__":
    predict('params.csv', ['theta0', 'theta1'])
