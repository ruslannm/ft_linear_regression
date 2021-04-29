# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/29 20:15:26 by rgero             #+#    #+#              #
#    Updated: 2021/04/29 22:02:33 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import ft_function as ft

def predict():

    user_input = input('Please enter a mileage: ')
    if ft.ft_is_number(user_input, 1, 'mileage'):
        mileage = float(user_input)
    else:
        exit(1)
    theta = (0, 0)
    if path.exists('params.csv'):
        df = ft.ft_read_csv('params.csv', ['theta0', 'theta1'])
        theta = (df.iloc[0]['theta0'], df.iloc[0]['theta1'])
    estimate_price = ft.estimateprice(theta, mileage)
    print(f'This car costs {round(estimate_price)}')

if __name__ == "__main__":
    predict()