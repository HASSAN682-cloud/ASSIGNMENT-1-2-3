Pseudocode and Tips

Below is the pseudocode to guide you through the steps for completing this assignment.



Function load_dataset(file_path):
    - Load dataset using pandas read_csv function
    - Display the first few rows of the dataset to ensure it's loaded correctly
    - Check for missing values and data types
    - Fill or drop missing values if necessary
    - Return cleaned dataset



Basic Data Analysis

Function analyze_data(dataset):
    - Compute summary statistics using .describe() for numerical columns
    - Group the data by a categorical column (e.g., species) and compute the mean for each group
    - Print summary statistics and group mean results
    - Identify interesting patterns or anomalies in the data
    - Return the analyzed data



Data Visualization

Function plot_line_chart(dataset):
    - Plot a line chart using matplotlib for a time-series column
    - Add labels, title, and legends
    - Display the plot

Function plot_bar_chart(dataset):
    - Group the data by a categorical column (e.g., species) and compute mean of a numerical column
    - Plot a bar chart for the mean values
    - Add labels, title, and legends
    - Display the plot

Function plot_histogram(dataset):
    - Plot a histogram for a numerical column to understand its distribution
    - Add labels and title
    - Display the plot

Function plot_scatter_plot(dataset):
    - Plot a scatter plot to visualize the relationship between two numerical columns
    - Add labels, title, and legends
    - Display the plot



Main Program

Main Function:
    - Call load_dataset() with the dataset file path
    - Call analyze_data() with the loaded dataset
    - Call each plot function: plot_line_chart(), plot_bar_chart(), plot_histogram(), plot_scatter_plot()
