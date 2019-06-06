# helpful example sites: 
# https://realpython.com/python-data-cleaning-numpy-pandas/
# http://www.developintelligence.com/blog/2017/08/data-cleaning-pandas-python/
# https://towardsdatascience.com/data-visualization-exploration-using-pandas-only-beginner-a0a52eb723d5

# this example shows importing some messy SDFB person data, dropping unnecessary columns and incomplete rows, some basic data checking/statistics/visualization, isolating people with extant birth and death dates, and exporting data

# import libraries needed for program, give shorter aliases so we don't have to type as much

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  #forces the popup to the top
import matplotlib.pyplot as plt

# read in and look at data from spreadsheet; N.B. "df" is short for "data frame" which is basically another name for tabular (spreadsheet) data
# in other words, "df" is basically a list of lists
# we use the . terminology to call a pre-built function from the library we imported

df = pd.read_csv("testData.csv")

# this is a function, it tells us information about "df"
type(df)
df

# head, tail, loc, etc. are methods and also use the . terminology because they are acting on "df" and can change "df"
df.head()
df.head(10)
df.tail()

df.loc[5]
df.loc[5][1]

# remove unnecessary columns cluttering up your dataset then double-check to make sure they're gone
# to_drop is a regular list - recognizable by square brackets - that contains three string objects
to_drop = ['occur_min_date','occur_max_date','NumDocAppearances']
to_drop
type(to_drop)
# here we see a method that alters df
df.drop(columns=to_drop, inplace=True) # or use df = df.drop(columns=to_drop) as either will replace the existing df with a version of df minus the dropped columns

df.loc[5]

# set dataset's unique identifiers (ODNB IDs) as locator IDs within this program and note how it changes the count of data types
# also notice the three different types of data: integers, strings, and "floats" aka numbers with decimal points

df.get_dtype_counts()

df['ODNB ID'].is_unique # check to make sure that the ODNB ID is a unique identifier before setting as the locator ID / index for df
df.set_index('ODNB ID', inplace=True) # or use df = df.set_index('ODNB ID') again either will replace the existing df with a new version

# df.loc[5] # only do this in class to show that it now generates an error because 5 is no longer a valid locator ID / index since it's not an ODNB ID
df.head()
df.loc[10000001]

df.get_dtype_counts()

# calculate some basic statistics on the float/number columns

number_columns = ['bio_length','bio_min_date','bio_max_date']

df[number_columns].count()
df[number_columns].max()
df[number_columns].min()
df[number_columns].median()
df[number_columns].mean()

# visualize the float/number columns as a histogram

df[number_columns].hist()
plt.show()

# identify null (blank) cells in your dataset and count them
# note that I can "chain" together methods, add them on top of each other
null_columns = df.columns[df.isnull().any()]
df[null_columns].isnull().sum()

# notice that isnull and notnull are inverses of each other

df['full_name'].isnull() # or df.isnull()['full_name']
df['full_name'].notnull()

# identify rows without name information and remove them, then double-check to make sure they're gone
# ***some of this code is superfluous, decide which way is clearer to present to students

df[df['full_name'].notnull()]
df[df['full_name'].notnull()].tail()
df.tail()
df = df[df['full_name'].notnull()]
df.tail()

# identify and remove rows without birth AND death information

df['full_date'].head()

full_date = df['full_date']
birth_death = full_date.str.contains('-') # N.B. this will also eliminate the uncommon variant of a comma instead of a '-' separating dates
                                            # ***this will silently substitute in a flourish date, might want to change code to prevent this?
birth_death[:5] #sneaky! strings are also lists!

df['full_date'] = np.where(birth_death, full_date, None) #if birth_death is true, will give us full_date, otherwise gives us None/empty cell

df = df[df['full_date'].notnull()]

# add a new column of death dates only

df['full_date'].str.split('-') # see what this split function does
split_date = df['full_date'].str.split('-') # save the results into a new variable
df['death_date'] = split_date.str[-1] # take the last date in the column and save it as a new 'death_date' column in the original dataframe

# use split the same way we removed everything before the dash character to remove non-numeric characters from 'death_date'

df['death_date']=df['death_date'].str.split(' ').str[-1] # removes everything before a space e.g. in the data instance of "d. 1610"
df['death_date']=df['death_date'].str.split('.').str[-1] # removes everything before a period e.g. in the data instance of "d.1610"
df['death_date']=df['death_date'].str.split('x').str[0] # removes everything after an x - note: this implies first death date in a range e.g. "1610x7" is a definitive death date
df['death_date']=df['death_date'].str.split('/').str[0] # removes everything after an / - note: this implies initial death date in a split date e.g. "1610/1" is a definitive death date
df['death_date']=df['death_date'].str.split('?').str[0] # removes everything after an ? - note: this implies an uncertain death date e.g. "1610?" is a definitive death date
df['death_date']=df['death_date'].str.split('s').str[0] # removes everything after an s - note: this implies an uncertain death date e.g. "1610s" is a definitive death date

# turn death dates into floats (numbers) and take average of death dates

df['death_date'] = pd.to_numeric(df['death_date'])
df['death_date'].mean() # note: how might the transformation of uncertain death dates (above) skew our results here?

# export current dataset to csv

df.to_csv('smallerTestData.csv')