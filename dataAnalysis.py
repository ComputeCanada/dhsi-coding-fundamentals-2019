# helpful example sites: https://realpython.com/python-data-cleaning-numpy-pandas/
# http://www.developintelligence.com/blog/2017/08/data-cleaning-pandas-python/
# https://towardsdatascience.com/data-visualization-exploration-using-pandas-only-beginner-a0a52eb723d5

# this example shows importing some messy SDFB person data, dropping unnecessary columns and incomplete rows, some basic data checking/statistics/visualization, isolating people with extant birth and death dates, and exporting data

# import libraries needed for program, give shorter aliases so we don't have to type as much

import pandas as pd
import numpy as np

# read in and look at data from spreadsheet; N.B. "df" is short for "data frame"

df = pd.read_csv("testData.csv")

df.head()
df.head(10)
df.tail()

df.loc[5]

# remove unnecessary columns cluttering up dataset

to_drop = ['occur_min_date','occur_max_date','NumDocAppearances']
df.drop(columns=to_drop, inplace=True) # or use df = df.drop(columns=to_drop)

df.loc[5]

# set dataset's unique identifiers as locator IDs within this program, note how it changes count of data types

df.get_dtype_counts()

df['ODNB ID'].is_unique
df.set_index('ODNB ID', inplace=True) # or use df = df.set_index('ODNB ID')

# df.loc[5] # only do this in class to show that it now generates an error
df.head()
df.loc[10000001]

df.get_dtype_counts()

# calculate statistics on number columns

number_columns = ['bio_length','bio_min_date','bio_max_date']

df[number_columns].count()
df[number_columns].max()
df[number_columns].min()
df[number_columns].median()
df[number_columns].mean()

# visualize is not working this is going to drive me bonkers will have to debug later

df.hist(column='bio_length')
df[number_columns].hist()

# filter rows without name information

null_columns = df.columns[df.isnull().any()]
df[null_columns].isnull().sum()

df['full_name'].isnull() # or df.isnull()['full_name']
df['full_name'].notnull()

df[df['full_name'].notnull()]
df[df['full_name'].notnull()].tail()
df.tail()
df = df[df['full_name'].notnull()]
df.tail()

# filter rows without birth AND death information

df['full_date'].head()

full_date = df['full_date']
birth_death = full_date.str.contains('-')
birth_death[:5]

df['full_date'] = np.where(birth_death, full_date, None)

df = df[df['full_date'].notnull()]

# turn full date into death dates only and take average

df['full_date'].str.split('-')
split_date = df['full_date'].str.split('-')

# df['full_date'] = split_date[1] # this is wrong and needs to be fixed so that I replace the full date with just the death date, ideally also filtering for ?s, c., etc.

# df['full_date'] = pd.to_numeric(df['full_date'])
# df['full_date'].mean()

# export current dataset to csv

df.to_csv('smallerTestData.csv')