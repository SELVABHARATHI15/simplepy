import pandas as pd

# Create sample data
data = {
    'Name': ['John', 'Emma', 'Alex', 'Sarah'],
    'Age': [28, 24, 32, 27],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [75000, 65000, 85000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('employees.csv', index=False)
print("CSV file created successfully!")

# Read the CSV file
read_df = pd.read_csv('employees.csv')

# Display the data
print("\nReading the CSV file:")
print(read_df)

# Basic operations with the DataFrame
print("\nBasic statistics:")
print(df.describe())

# Filter data (employees with salary > 70000)
high_salary = df[df['Salary'] > 70000]
print("\nEmployees with high salary:")
print(high_salary)

# Sort data by age
sorted_by_age = df.sort_values(by='Age')
print("\nData sorted by age:")
print(sorted_by_age)

# Calculate average salary
avg_salary = df['Salary'].mean()
print(f"\nAverage salary: ${avg_salary:,.2f}")