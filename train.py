# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/30 19:58:59 by rgero             #+#    #+#              #
#    Updated: 2021/04/30 21:26:03 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import ft_function as ft

def ft_mean(l):
    return sum(l) / len(l)

def ft_std(l):
    mean = ft_mean(l)
    diff = 0
    len_l = len(l)
    for i in l:
        diff = diff + (i - mean) ** 2
    return (diff / len_l) ** 0.5    

def get_value(filename, df, column):
    norm_l = []
    l = df[column].tolist()
    mean = ft_mean(l)
    std = ft_std(l)
    for i in l:
         if i < 0:
              print(f'\nError: {column} is negative in the file {filename}')
              exit(1)
         norm_l.append((i - mean) / std)
    return ((norm_l, mean, std))

def train(filename, columns):
    if path.exists(filename):
        df = ft.ft_read_csv(filename, columns)
        x = get_value(filename, df, columns[0])
        y = get_value(filename, df, columns[1])
    else:
        print(f'\nError: {filename} is missing')
        exit(1)

if __name__ == "__main__":
    train("data.csv", ['km', 'price'])