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

#read csv data into pandas DataFrame with column names as col_names
col_names = ['sepal_length','sepal_width','petal_length','petal_width','class']

iris =pd.read_csv('iris.csv', header=None, names=col_names)
#show first 5 rows of dataFrame
print(iris.head())


##############Part 4.1 ############
#.info shows information on each of the columns, such as the data type and number of missing values. There is no missing values in the data set
print(iris.info)

datatypes = iris.dtypes
#describe() prints descriptive statistics of data set
print(iris.describe())

#unique() method on the 'Class' column to show how many different class or species of Iris flower is in the data set.
unique_iris =iris['class'].unique()
print(unique_iris)

print(f"First five lines of dataset are {iris.head()} ")
print(f"Last five lines of dataset are {iris.tail()} ")
print(f'Summary of data :')
print(iris.describe())



'''I assigned code that do analysis to variables because
 when I will do the output to .txt program will not repeat calculation
 but just write the result to txt
 Reference for pivot_table and group by: Data Camp Data Manupulating with Pandas
 '''

pivot_table = iris.pivot_table(index='class', 
                               values=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], aggfunc=np.mean)
print(pivot_table)
print(list(iris.columns.values))

'''We can summary each var with pivot table using different numpy fuction but we also can use group by'''


print("Using pands groupby function to split the iris dataframe by Class of iris species \n")
# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("class")

# compute count of group, excluding missing values
countbyclass = iris.groupby("class").count()


# Groupby class of Iris plant and return the mean of the remaining columns in each group.

meanbyclass = iris.groupby('class').mean()

# get max of group values
maxbyclass= iris.groupby("class").max()


# get min of group values
minbyclass=iris.groupby("class").min()

#get summary statistics for each class of iris plant in the dataset can be obtained using the describe method on the GroupByobject.
describebyclass = iris.groupby("class").describe()
print(describebyclass)


#########SAVE to txt file############### 
FILENAME = "analysis.txt"
with open(FILENAME, 'wt') as f:
    f.write("IRIS DATASET ANALYSIS \n")

    
    f.write("First five lines of dataset are:   \n")
    f.write(str(iris.head()))


    f.write("Last five lines of dataset are:   \n")
    f.write(str(iris.tail()))

    f.write(f'Show all unique values : \n')
    f.write(str(unique_iris))
    f.write("   \n")
    f.write(f'Data types in Iris DataFrame is : \n')
    f.write(str(datatypes))


    f.write("   \n")
    f.write('Summary of data :  \n')
    f.write("   \n")
    f.write(str(iris.describe()))
    f.write('\n   \n')

    f.write(" Pivot table analysis of each class of iris:  \n")
    f.write(str(pivot_table))
    f.write('\n   \n')
    f.write("The number of observations for each variable for each Iris species in the data set are as follows: \n")
    f.write(str(countbyclass))
    f.write('\n   \n')
    f.write("The mean or average measurement for each group of Iris Species in the dataset is: \n")
    f.write(str(meanbyclass))
    f.write('\n   \n')
    f.write("The maximum value for each measurement for each Class of Iris plant in the Iris dataset are:  \n")
    f.write(str(maxbyclass))
    f.write('\n   \n')
    f.write("The minimum value for each measurement for each Class of Iris plant in the Iris dataset are:\n")
    f.write('\n   \n')
    f.write(str(minbyclass))
    f.write('\n   \n')
    f.write('Summary of each variable of each class:   \n')
    f.write(str(describebyclass))









#2.Saves a histogram of each variable to png files, and
iris['sepal_length'].hist(bins=30) #plot the histogram of sepal lenght
plt.title('Histogram of sepal lenght') #title of histogram
plt.xlabel('Sepal lenght in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_sepallenght.png') #save plot
plt.show() #show the histogram

iris['sepal_width'].hist(bins=30) #plot the histogram of sepal_width
plt.title('Histogram of sepal_width') #title of histogram
plt.xlabel('Sepal width in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_sepal_width.png') #save plot
plt.show() #show the histogram

iris['petal_length'].hist(bins=30) #plot the histogram of petal_length
plt.title('Histogram of petal length') #title of histogram
plt.xlabel('Petal length in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_petal_length.png') #save plot
plt.show() #show the histogram


iris['petal_width'].hist(bins=30) #plot the histogram of petal_width
plt.title('Histogram of petal_width') #title of histogram
plt.xlabel('Petal width in cm') #x axis label
plt.ylabel('Number of sample') #y axis label
plt.savefig('images/iris_hist_petal_width.png') #save plot
plt.legend()
plt.show() #show the histogram


iris.hist() #histogram plot for all variables
plt.savefig('images/iris_main_hist.png')  # save plot
plt.show() #show plot

########## Scatter plot of each pair of variables
#Idea reference is Data Camp Course 4

ax = iris[iris['class']== "Iris-setosa"].plot(x='petal_length', y="petal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='petal_length', ax=ax, y="petal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='petal_length', ax=ax, y="petal_width", kind= 'scatter', c='blue')

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Petal Sizes")
plt.savefig('images/scatter_petal_lenghtvswidth_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
plt.show() #show scatter plot

# scatter plot for pair of parameters  'sepal_length','sepal_width'
ax = iris[iris['class']== "Iris-setosa"].plot(x='sepal_length', y="sepal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='sepal_length', ax=ax, y="sepal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='sepal_length', ax=ax, y="sepal_width", kind= 'scatter', c='blue')

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Sepal Sizes")
plt.savefig('images/scatter_sepal_lenghtvswidth_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
plt.show() #show scatter plot




ax = iris[iris['class']== "Iris-setosa"].plot(x='sepal_length', y="petal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='sepal_length', ax=ax, y="petal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='sepal_length', ax=ax, y="petal_width", kind= 'scatter', c='blue')

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris Sepal Length / Petal Width")
plt.savefig('images/scatter_sepal_lenghtvspetalwidth_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
plt.show() #show scatter plot

ax = iris[iris['class']== "Iris-setosa"].plot(x='petal_length', y="sepal_width", kind= 'scatter', c='red')
iris[iris['class']== "Iris-versicolor"].plot(x='petal_length', ax=ax, y="sepal_width", kind= 'scatter', c= 'green')
iris[iris['class']== "Iris-virginica"].plot(x='petal_length', ax=ax, y="sepal_width", kind= 'scatter', c='blue')

plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.title("Iris Petal Length / Sepal Width")
plt.savefig('images/scatter_petal_lenghtvssepal_width_allclasses.png')  # save plot
plt.legend(["Iris-setosa", "Iris-versicolor", 'Iris-virginica'])
plt.show() #show scatter plot