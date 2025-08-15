import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'Sales': [100, 150, 200, 180, 220],
        'Species': ['Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica'],
        'PetalLength': [1.0, 1.2, 2.0, 3.0, 4.0],
        'SepalLength': [5.0, 4.5, 5.5, 6.0, 7.0]}

# Create a DataFrame
df = pd.DataFrame(data)

# Line chart showing sales trends over time
plt.figure(figsize=(8, 5))
plt.plot(df['Date'], df['Sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trends Over Time')
plt.show()

# Bar chart showing average petal length per species
plt.figure(figsize=(8, 5))
avg_petal_length = df.groupby('Species')['PetalLength'].mean()
avg_petal_length.plot(kind='bar')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.title('Average Petal Length by Species')
plt.show()

# Histogram of Petal Length
plt.figure(figsize=(8, 5))
plt.hist(df['PetalLength'], bins=10)
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Distribution of Petal Length')
plt.show()

# Scatter plot showing relationship between sepal length and petal length
plt.figure(figsize=(8, 5))
plt.scatter(df['SepalLength'], df['PetalLength'])
plt.xlabel('Sepal Length')
plt.ylabel('PetalLength')
plt.title('Relationship between Sepal Length and Petal Length')
plt.show()