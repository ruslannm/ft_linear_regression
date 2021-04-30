# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_function.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/29 20:02:55 by rgero             #+#    #+#              #
#    Updated: 2021/04/30 20:42:18 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import numpy as np
import pandas as pd

def ft_read_csv(filename, columns):

    is_correct = 0
    if path.exists(filename):
        df = pd.read_csv(filename)
        if list(df.columns) == columns:
            for y in df.columns:
                if(df[y].dtype == np.float64 or df[y].dtype == np.int64)\
                and df.isnull().sum()[y] == 0:
                    is_correct += 1
    if is_correct == len(columns):                
        return df
    else:
        print('\nError: The content of the file {} doesn\'t respect the norme'\
              .format(filename))
        exit(1)

def ft_is_number(str, only_positive, str_name):
    try:
        float(str)
        if only_positive and float(str) < 0:
            print('\nError: {} must be only positive'.format(str_name))
            return False
        return True
    except ValueError:
        print('\nError: {} must be number'.format(str_name))
        return False

def estimateprice(theta, mileage):
    return theta[0] + theta[1] * mileage


if __name__ == "__main__":
    ft_read_csv('params.csv', ['theta0', 'theta1'])