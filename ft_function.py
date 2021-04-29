# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_function.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/29 20:02:55 by rgero             #+#    #+#              #
#    Updated: 2021/04/29 20:20:28 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#from os import path
import pandas as pd

def get_cfg(filename):
	if not path.exists(filename):
        print(f'\nError: config file "{filename}" not found!')
        exit(1)

	df = pd.read_csv('ft_linear_regression.cfg')
	print(df.head())
	


def estimateprice(teta0, teta1, mileage):
	return teta0 + teta1 * mileage

#def get_param():

if __name__ == "__main__":
	get_cfg()