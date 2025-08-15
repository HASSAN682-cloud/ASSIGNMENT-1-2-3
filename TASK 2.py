import pandas as pd

# Create a sample DataFrame
data = {'ColumnA': [10, 12, 15, 12, 18, 20],
        'ColumnB': [5.1, 5.5, 6.0, 5.8, 6.2, 5.0],
        'ColumnC': ['apple', 'banana', 'orange', 'apple', 'banana', 'orange']}
df = pd.DataFrame(data)

# Compute basic statistics using .describe()
summary_statistics = df.describe()

# Print the resulting summary
print(summary_statistics)