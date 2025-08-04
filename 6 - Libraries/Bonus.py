import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('grades.csv')

# Show first few rows and column names for debugging
print("Data Preview:")
print(df.head())
print("\nColumns in CSV:")
print(df.columns)

# Ensure column names are correct
required_columns = ['Networking', 'Data Structures', 'GIS']
if not all(col in df.columns for col in required_columns):
    raise ValueError("One or more required columns are missing in the CSV.")

# Bar Chart: Average score pe
df['Average'] = df[required_columns].mean(axis=1)

plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Average'], color='skyblue')
plt.title('Average Score per Student')
plt.xlabel('Student')
plt.ylabel('Average Score')
plt.tight_layout()
plt.savefig('average_score_bar_chart.png')
plt.show()
plt.close()

# Line Chart: Trend of Networking scores
plt.figure(figsize=(8, 5))
plt.plot(df['Name'], df['Networking'], marker='o', linestyle='-', color='green')
plt.title('Networking Score Trend')
plt.xlabel('Student')
plt.ylabel('Networking Score')
plt.tight_layout()
plt.savefig('Networking_score_line_chart.png')
plt.show()
plt.close()

# Histogram: Data Structures scores
plt.figure(figsize=(8, 5))
plt.hist(df['Data Structures'], bins=5, color='salmon', edgecolor='black')
plt.title('Distribution of Data Structures Scores')
plt.xlabel('Data Structures Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('Data_Structures_score_histogram.png')
plt.show()
plt.close()

print("\nAll plots saved successfully!")
