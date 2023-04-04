import pandas as pd

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris =  pd.read_csv(csv_url)

print(iris.head())