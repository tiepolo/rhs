import pandas as pd

# Load the CSV file
df = pd.read_csv('user_data_raw.csv')

# Define a function to extract specific keys from JSON
def extract_key(json_str, key):
    try:
        data = eval(json_str)  # Using eval to convert the JSON string to a dictionary
        return data.get(key)
    except (NameError, SyntaxError):
        return None

# Define the columns and keys you want to extract
columns_and_keys = {
    'address': 'first',
    'phone': 'number'
}

# Extract specific keys and create new columns for each key
for col, key in columns_and_keys.items():
    df[f'{col}_{key}'] = df[col].apply(lambda x: extract_key(x, key))

# Drop the original JSON columns
df.drop(columns=columns_and_keys.keys(), inplace=True)

# Now, you have the extracted keys as separate columns

# Print the DataFrame with the extracted columns
print(df)

# Save the modified DataFrame to a new CSV file (optional)
df.to_csv('user_data_parsed.csv', index=False)