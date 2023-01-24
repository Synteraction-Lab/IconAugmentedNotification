# coding=utf-8

# pip3 install pandas

# command format: python3 csv_to_anova.py file_name.csv 'index_column' 'group_by_column' 'interested_data'

import sys
import optparse
import pandas as pd
import os


def csv_to_anova(file_name, index_column, group_by_column, interested_data_column):

    df = pd.read_csv(file_name, header=0)
    df_wide = df.pivot(index=index_column, columns=group_by_column, values=interested_data_column)

    # print(df)
    # print(df_wide)

    file_path = os.path.splitext(file_name)
    file_name_wide_format = f'{file_path[0]}-{interested_data_column}{file_path[1]}'

    df_wide.to_csv(file_name_wide_format)
    print(f'See the file: [{file_name_wide_format}]')


parser = optparse.OptionParser()
options, args = parser.parse_args()

# print('options:', options)
# print('args:', args)

if len(args) < 4:
    print('Missing arguments!')
    print(
        "e.g.: python3 csv_to_anova.py file_name.csv 'index_column' 'group_by_column' 'interested_data_column'")
    sys.exit(0)



csv_to_anova(args[0], args[1], args[2], args[3])
