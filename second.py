import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 92, 78],
    'English': [88, 79, 95]
}


df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Calculate the mean for each subject
print("\nAverage scores:")
print(df[['Math', 'English']].mean())

# Calculate the total score for each student
df['Total'] = df['Math'] + df['English']
print("\nWith totals:")
print(df)