### pands-project
### project for Programming and Scripting 

# Table of Contents
<a name="-table-of-contents"></a>

1. [Introduction to the project](#1.-introduction-to-the-project) 
2. [The Fisher Iris Data Set](#2.-the-fisher-iris-dataset) 
3. [Downloading the Fisher Iris dataset](#3.-download-the-fisher-iris-dataset)
4. [Program analysis.py](#4.-program-analysis-python)

    4.1. [Output of summary of each variable to analysis.txt](#4.1.-output-of-summary-of-each-variable)

    4.2.[Histograms of each variable as .png](#4.2.-histogram-of-each-variable-as-png)

    4.3.[Scatter plots of each pair of variable](#4.3.-scatter-plots-of-each-variable)

5. [Summary and Conclusions](#5.-summary-and-conclusions)
6. [References](#6.-references)



# 1. Introduction to the project
<a name="1.-introduction-to-the-project"></a>

This project was made during Programming and Scripting module (Higher Diploma in Computing in Data Analytics) at ATU Galway. 

Task that was given: 

"You might do that for this project as follows:
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
    1. Outputs a summary of each variable to a single text file,
    2. Saves a histogram of each variable to png files, and
    3. Outputs a scatter plot of each pair of variables.
    4. Performs any other analysis you think is appropriate


Also, It might help to suppose that your manager has asked you to investigate the data set, with a
view to explaining it to your colleagues. Imagine that you are to give a presentation on the
data set in a few weeks’ time, where you explain what investigating a data set entails and how
Python can be used to do it. You have not been asked to create a deck of presentation slides,
but rather to present your code and its output to them.


# 2. The Fisher Iris Data Set Research Online
<a name="2.-the-fisher-iris-dataset"></a>

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. Fisher's paper was published in the Annals of Eugenics and includes discussion of the contained techniques' applications to the field of phrenology.[Wikipedia page about dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-5)

The Iris dataset is a popular dataset used in machine learning and data science. It consists of 150 observations of iris flowers, with 50 observations for each of the three species - Setosa, Versicolor, and Virginica. The dataset includes four features - sepal length, sepal width, petal length, and petal width.

The Pandas Iris project involves using the Pandas library, which is a popular data manipulation tool in Python, to analyze and visualize the Iris dataset. With Pandas, we can load the dataset into a Pandas DataFrame, which is a two-dimensional table-like data structure.

Using Pandas, we can easily perform data cleaning, data preprocessing, and data analysis on the Iris dataset. For example, we can use Pandas to drop any rows with missing data, rename columns, calculate summary statistics, and visualize the data using various charts and graphs.

The Pandas Iris project is a great way to learn and practice data manipulation, data analysis, and data visualization skills using a real-world dataset. With the popularity of Pandas and the widespread use of the Iris dataset, it is an ideal project for beginners and advanced users alike.

In conclusion, the Pandas Iris project is a great way to learn and practice data science skills using a popular dataset. By using Pandas, we can easily manipulate and analyze the data, helping us gain insights and make data-driven decisions.


Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica




# 3. Downloading the Fisher Iris dataset <a name="3.-download-the-fisher-iris-dataset"></a>

I used Python programming language and Pands package that is built on top of it. 

Dataset was downloaded from http://archive.ics.uci.edu/ml/datasets/Iris 

On the top of analysis.py I added all packages that I will work with. 
 
- [Pandas.pydata documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html) 
- [Matplotlib documentation](https://matplotlib.org/index.html) 
- [Numpy documentation](https://numpy.org/doc/)


I used Pandas module to read dataset in csv format. 
Data is stored in csv (comma-separated values) file and when we read it with Pandas we create Pandas DataFrame. 

DataFrame is amazing for data analysis of real world date because we can store all types of data and do calculation on columns and lines. 

`read_csv` - Read a comma-separated values (csv) file into DataFrame.

`
col_names = ['sepal_length','sepal_width','petal_length','petal_width','class']
iris =pd.read_csv('iris.csv', header=None, names=col_names)
`



# 4. Program analysis.py
<a name="4.-program-analysis-python"></a>


# 4.1. Output of summary of each variable to analysis.txt
<a name="4.1.-output-of-summary-of-each-variable"></a>

One of many ways to output summary of each variable is pivot_tables. 
The "values" argument is the column that we want to summarize, and the index column is the column that you want to group by. By default, pivot_table takes the mean value for each group. 


One of the most popular to output statistical summary of dataset is describe() 
The pandas describe() function shows the following:

The `count` or number of the non-NA/null observations in the dataset.

The `max` shows the maximum of the values and the min shows the minimum of the values.

The `mean` shows the mean or average of the values (the sum of data values divided by total number of values).
The `std` shows the standard deviation  of the observations.

The describe function also shows the 25th, 50th and 75th percentiles. 
The 25th percentile shows the percentage of values falling below that percentile. 
The 50th percentile shows the same information as the median would, that is where 50% of the values fall above and 50% fall below the value.


Then after computing summary statistics over each class of Iris I create txt file and write all results into it
```
FILENAME = "analysis.txt"
with open(FILENAME, 'wt') as f:
    f.write("IRIS DATASET ANALYSIS \n")

```

in file analysis.txt next information can be found:
    

    
    - First five lines of dataset
    - Last five lines of dataset are
    - unique values
    - data types in Iris DataFrame
    - Summary of data 
    - Pivot table analysis of each class of iris
    - The number of observations for each variable for each Iris species in the data set
    - The mean or average measurement for each group of Iris Species in the dataset
    - The maximum value for each measurement for each Class of Iris plant in the Iris dataset
    - The minimum value for each measurement for each Class of Iris plant in the Iris dataset 
    -Summary of each variable of each class




# 4.2. Histograms of each variable as .png 
<a name="4.2.-histogram-of-each-variable-as-png"></a>

All plots saved to folder images as .png files

Plots that are created shows :
1.Histogram of sepal lenght

2. Histogram of sepal width
3. Histogram of petal lenght
4. Histogram of petal width

5. Histogram for all variables



# 4.3. Scatter plots of each pair of variable
<a name="4.3.-scatter-plots-of-each-variable"></a>



1. Scatter plot - Iris petal sizes
2. Scatter plot - Iris sepal sizes
3. Scatter plot - Iris sepal width\petal lenght 
4. Scatter plot - Iris petal width\sepal lenght

Also, different colours of dots mark different classes
(Iris Setosa, Iris Versicolour, Iris Virginica)

# 5. Summary and Conclusions<a name="#5.-summary-and-conclusions"></a>

The provided code performs analysis on the Iris dataset using the pandas library. Here's a summary of the work done:

The code imports the necessary libraries: pandas, numpy, and matplotlib.

The Iris dataset is read from a CSV file into a pandas DataFrame, with column names assigned.

Information about the dataset is displayed using info() and describe() methods.

The unique classes or species of Iris flowers in the dataset are identified using the unique() method.

Various statistics are computed using the groupby() function and stored in variables, including counts, means, maximums, and minimums for each class of Iris plant.

Summary statistics for each class of Iris plant are obtained using the describe() method on the GroupBy object.

The analysis results are saved to a text file named "analysis.txt" using the write() method.

Following the analysis, the code generates several visualizations:

- Histograms of each variable (sepal length, sepal width, petal length, petal width) are saved as PNG files.
- Scatter plots are created to visualize relationships between different pairs of variables: petal length vs. petal width, sepal length vs. sepal width, sepal length vs. petal width, and petal length vs. sepal width. Each scatter plot includes data points for the three classes of Iris plants, distinguished by color. The scatter plots are also saved as PNG files.


Overall, the code performs exploratory data analysis on the Iris dataset, including descriptive statistics, group analysis, and visualization.




# 6. References <a name="#6.-references"></a>

- Website: [Python 3 documentation](https://docs.python.org/3/index.html) Official Python 3 Documentation at <https://docs.python.org>
- Website: [Getting Started with pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html) Official `pandas` tutorial  at <https://pandas.pydata.org>

- Website: [Numpy Documentation ](https://numpy.org/doc/) https://numpy.org/doc/

- Website: [DataCamp Data Manipulation with Pands](https://app.datacamp.com/learn/courses/data-manipulation-with-pandas) learning course at <https://app.datacamp.com/learn/courses/data-manipulation-with-pandas>

- Website [wikipedia page about dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-5) https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-5