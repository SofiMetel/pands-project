import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

print(f"First five lines of dataset are {iris.head()} ")
print(f"Last five lines of dataset are {iris.tail()} ")
print(f'Summary of data :')
print(iris.describe())

# I took  Pivot tables idea from DataCamp course #4
print(iris.pivot_table(index='class', values=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], aggfunc=np.mean))
print(list(iris.columns.values))

#2.Saves a histogram of each variable to png files, and
iris['sepal_length'].hist(bins=30) #plot the histogram of sepal lenght
plt.title('Histogram of sepal lenght') #title of histogram
plt.xlabel('Sepal lenght in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_sepallenght.png') #save plot
#plt.show() #show the histogram

iris['sepal_width'].hist(bins=30) #plot the histogram of sepal_width
plt.title('Histogram of sepal_width') #title of histogram
plt.xlabel('sepal_width in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_sepal_width.png') #save plot
plt.show() #show the histogram

iris['petal_length'].hist(bins=30) #plot the histogram of petal_length
plt.title('Histogram of petal_length') #title of histogram
plt.xlabel('petal_length in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_petal_length.png') #save plot
plt.show() #show the histogram


iris['petal_width'].hist(bins=30) #plot the histogram of petal_width
plt.title('Histogram of petal_width') #title of histogram
plt.xlabel('petal_width in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_petal_width.png') #save plot
plt.legend()
plt.show() #show the histogram


iris.hist() #histogram plot for all variables
plt.savefig('images/iris_main_hist.png')  # save plot
#plt.show() #show plot



versicolor = iris[iris['class'] == "Iris-versicolor"]
print(versicolor)
setosa = iris[iris['class']== "Iris-setosa"]
virginica = iris[iris['class'] == 'Iris-virginica']

'''

points = plt.scatter(versicolor['petal_length'], versicolor["petal_width"], label="Iris-versicolor", facecolor = 'green')
plt.scatter(setosa['petal_length'], setosa["petal_width"], label="Iris-setosa", marker='x', facecolor='blue')
plt.scatter(virginica['petal_length'], virginica["petal_width"], label='Iris-virginica', marker='s', facecolor='red')
'''

iris.plot(x='petal_length', y="petal_width", kind= 'scatter')

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Petal Sizes")
plt.savefig('images/scatter_petal_lenghtvswidth.png')  # save plot
plt.legend()
#plt.show()


## Scatter plot of each pair of variables
#Idea reference is Data Camp Course 4

ax = iris[iris['class']== "Iris-setosa"].plot(x='petal_length', y="petal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='petal_length', ax=ax, y="petal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='petal_length', ax=ax, y="petal_width", kind= 'scatter', c='blue')

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Petal Sizes")
plt.savefig('images/scatter_petal_lenghtvswidth_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
#plt.show() #show scatter plot

# scatter plot for pair of parameters  'sepal_length','sepal_width'
ax = iris[iris['class']== "Iris-setosa"].plot(x='sepal_length', y="petal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='sepal_length', ax=ax, y="petal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='sepal_length', ax=ax, y="petal_width", kind= 'scatter', c='blue')

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Sepal Sizes")
plt.savefig('images/scatter_sepal_lenghtvswidth_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
plt.show() #show scatter plot