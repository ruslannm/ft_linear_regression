# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rgero <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/04/29 20:15:26 by rgero             #+#    #+#              #
#    Updated: 2021/04/29 20:37:51 by rgero            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import pandas as pd

def read_params(filename):

    theta = [0, 0]
    if path.exists(filename):
        df = pd.read_csv(filename, header = None)
        print(len(df.columns))
#        for y in agg.columns:
#            if(df[y].dtype == np.float64 or agg[y].dtype == np.int64):
#          treat_numeric(agg[y])
#    else:
#          treat_str(agg[y])

        print(df.head())
    return theta

if __name__ == "__main__":
    read_params('params.csv')