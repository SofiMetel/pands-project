import pandas as pd
'''
Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica
'''
col_names = ['sepal_length','sepal_width','petal_length','petal_width','class']

iris =pd.read_csv('iris.csv', header=None, names=col_names)
print(iris.head())

print(iris.info())
print('.info() shows information on each of the columns, such as the data type and number of missing values. There is no missing values in the data set')

print(iris.describe())
print(iris.dtypes)
print(iris['class'].unique())