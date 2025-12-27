import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

# Adding new rows to df
new_rows = [
    {'Name': 'GF1', 'Age': 20, 'City': 'City1'},
    {'Name': 'GF2', 'Age': 30, 'City': 'City2'},
    {'Name': 'GF3', 'Age': 40, 'City': 'City3'}
]
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

# Update Alice's info
alice_row = df[df['Name'] == 'Alice'].copy()
alice_row['Name'] = 'GF1 (Ex-Alice)'
new_alice_row = {'Name': 'Alice, GF: GF4', 'Age': 25, 'City': 'New York'}
df = df[df['Name'] != 'Alice']
df = pd.concat([df, alice_row, pd.DataFrame([new_alice_row])], ignore_index=True)

# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")