pip install request

import pandas as pd

# 1. Load the dataset
# You can replace 'iris.csv' with the path to your chosen CSV file.
# For demonstration, we'll assume 'iris.csv' is in the same directory.
try:
    df = pd.read_csv('iris.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'iris.csv' not found. Please ensure the file is in the correct directory or provide the full path.")
    # As a fallback for demonstration if the file isn't present,
    # we can create a dummy DataFrame or load from a public source if available.
    # For a real scenario, you'd need the actual file.
    data = {
        'sepal_length': [5.1, 4.9, 6.3, 5.0, 5.5],
        'sepal_width': [3.5, 3.0, 3.3, 3.4, 2.3],
        'petal_length': [1.4, 1.4, 6.0, 1.5, 4.0],
        'petal_width': [0.2, 0.2, 2.5, 0.2, 1.3],
        'species': ['setosa', 'setosa', 'virginica', 'setosa', 'versicolor']
    }
    df = pd.DataFrame(data)
    print("Using a dummy DataFrame for demonstration.")


# 2. Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# 3. Explore the structure of the dataset
print("\nDataset information (data types and non-null counts):")
print(df.info())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 4. Clean the dataset (handling missing values)
# For demonstration, we'll introduce some missing values artificially
# to show the cleaning process.
df.loc[1, 'sepal_width'] = None
df.loc[3, 'petal_length'] = None

print("\nMissing values after artificial introduction:")
print(df.isnull().sum())

# Option 1: Fill missing values (e.g., with the mean of the column)
# This is suitable for numerical columns.
for col in df.select_dtypes(include=['number']).columns:
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(), inplace=True)
        print(f"Filled missing values in '{col}' with its mean.")

# Option 2: Drop rows with missing values
# Uncomment the line below if you prefer to drop rows with any missing values.
# df.dropna(inplace=True)
# print("\nDataset after dropping rows with missing values.")

print("\nMissing values after cleaning:")
print(df.isnull().sum())