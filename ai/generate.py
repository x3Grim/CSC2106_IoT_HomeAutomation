import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows in the dataset
num_rows = 1000

# Generate pressure values for 100 columns (pressure1, pressure2, ..., pressure100)
pressure_columns = ['pressure' + str(i) for i in range(1, 101)]
pressure_values = np.random.randint(800, 1200, size=(num_rows, 100))

# Create DataFrame with pressure columns
df = pd.DataFrame(pressure_values, columns=pressure_columns)

# Generate sleep column with values 1 (asleep) or 0 (not asleep)
df['sleep'] = np.random.choice([0, 1], size=num_rows)

# Display the first few rows of the generated dataset
print(df.head())

# Save the dataset to a CSV file
df.to_csv('dummy_dataset.csv', index=False)