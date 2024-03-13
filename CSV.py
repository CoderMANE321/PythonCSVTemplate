import pandas as pd
import numpy as np
import os  # Import the os module

# Get the current working directory
current_dir = os.getcwd()

# Define the relative path to the CSV file
csv_file_path = os.path.join(current_dir, 'PythonAnalysis', 'data.csv')

# Check if the file exists before loading it
if os.path.isfile(csv_file_path):
    # Load CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Display the first few rows of the DataFrame
    print("Original Data:")
    print(df.head())

    # Perform basic analysis using calculus and linear algebra
    mean_values = df.mean()  # Calculate mean for each column
    sum_values = df.sum()    # Calculate sum for each column
    transpose_data = df.T    # Transpose the DataFrame
    covariance_matrix = df.cov()  # Calculate covariance matrix

    # Display the results
    print("\nMean Values:")
    print(mean_values)

    print("\nSum Values:")
    print(sum_values)

    print("\nTransposed Data:")
    print(transpose_data.head())

    print("\nCovariance Matrix:")
    print(covariance_matrix)

    # You can add more analysis or operations based on your specific requirements
else:
    print(f"File not found: {csv_file_path}")
