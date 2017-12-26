# 7 B
#Load the Titanic Dataset into one of the data structures (NumPy or Pandas). Do the following for this data set:
# a)   Display header rows and description of the loaded dataset.
# b)   Remove unnecessary features (E.g. drop unwanted columns) from the dataset.
# c)   Manipulate data by replacing empty column values with a default value.
# d)   How many entries does this dataset have?
# e)   How many attributes does this data set have?
# f)    List the attributes
# g)   What are the data types of the attributes?
# h)   What is the minimum and maximum age of the passengers in the data set?
# i)     What is the mean value of the "Age" attribute?
# j)    Plot a histogram depicting the number of people of a particular age
# k)   Label the x and y axis of this plot
# l)     What is the default graph plotted by a dataframe?


import pandas as pd
import numpy as np
import seaborn as sns
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# get titanic & test csv files as a pandas DataFrame
titanic_df = pd.read_csv("train.csv")

#a)Display header rows and description of the loaded dataset.

print("======Data Headers=======")
titanic_df.head()

print("=====Data Description=====")
# column description
titanic_df.info()
titanic_df.describe()

#b) Remove unnecessary features (E.g. drop unwanted columns) from the dataset.

titanic_df = titanic_df.drop(['PassengerId', 'Name', 'Ticket'], axis=1)

# Another way of dropping columns done in place, that is a new variable is not required.
titanic_df.drop(['Parch'], axis=1, inplace=True)

print("=====Check if columns were really dropped=====")
# print dataframe again to see how the contents look like
titanic_df.head()

#c) Manipulate data by replacing empty column values with a default value.

# Next look for columns which have missing values. Fill those cells with some sort of default value(should be similar to other values in the colums)

titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
# Check if there are no missing values
print(titanic_df["Embarked"])

#d) How many entries does this dataset have?

print("Number of rows in the data frame is ",len(titanic_df))

#e)How many attributes does this data set have?

print("Number of columns in the data frame is ",len(titanic_df.columns))

#h) What is the minimum and maximum age of the passengers in the data set?

print("Minimum Age is", titanic_df.Age.min())
print("Maximum Age is", titanic_df.Age.max())

#i) What is the mean value of the "Age" attribute?

print ("Mean value of Age is", titanic_df.Age.mean())
print("Std Deviation of Age is", titanic_df.Age.std())

# ----------- VISUALIZATIONS ---------#

#j) Plot a histogram depicting the number of people of a particular age

titanic_df.Age.hist()
plt.show()

#k) Label the x and y axis of this plot
ax1= titanic_df.Age.hist()
ax1.set(xlabel='Age', ylabel='Number of people')

plt.show()

# l) What is the default graph plotted by a dataframe?
ax2= titanic_df.Age.plot() # It is a line-graph
#ax2.set(xlabel='nth row in datset', ylabel='Age')

plt.show()
