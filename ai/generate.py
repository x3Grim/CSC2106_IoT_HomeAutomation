import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows in the dataset
num_rows = 1000

# Generate pressure values for 100 columns (pressure1, pressure2, ..., pressure100)
pressure_columns = ['pressure' + str(i) for i in range(1, 101)]
pressure_values = np.random.randint(0, 4096, size=(num_rows, 100))

# Create DataFrame with pressure columns
df = pd.DataFrame(pressure_values, columns=pressure_columns)

# Calculate the total pressure for each row
df['total_pressure'] = df.sum(axis=1)

# Generate sleep column based on the condition
df['sleep'] = np.where(df.index < num_rows // 2, 0, 1)

# Display the first few rows of the generated dataset
print(df.head())

# Save the dataset to a CSV file
df.to_csv('dummy_dataset.csv', index=False)
