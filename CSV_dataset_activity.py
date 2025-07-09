import pandas as pd

# Step 1: Choose a dataset file
dataset_files = {
    1: 'video_game_sales_1.csv',
    2: 'video_game_sales_2.csv',
    3: 'video_game_sales_3.csv'
}

# Simulate user selection (change this value to 2 or 3 as needed)
selected_option = 1
selected_file = dataset_files.get(selected_option)

# Step 2: Read the selected CSV file
df = pd.read_csv(selected_file)

# Step 3: Perform analysis
print("First few rows of the dataset:")
print(df.head())

print("\nDataset dimensions (rows, columns):", df.shape)

print("\nData types and missing values:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print()
df.pivot_table(values='Global_Sales', index='Genre', columns='Platform', aggfunc='mean')

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nAre there any duplicates?")
print(df.duplicated().sum())

# Optional: Remove duplicates (if any)3
df = df.drop_duplicates()

import matplotlib.pyplot as plt  # Only needed once at the top of your file

# Step 1 – Sort the data by Global Sales (so biggest bars are at the bottom)
df_sorted = df.sort_values(by='Global_Sales', ascending=True)

# Step 2 – Create a non-horizontal bar chart
plt.figure(figsize=(10, 6))  # Sets the size of the chart
plt.bar(df_sorted['Title'], df_sorted['Global_Sales'])  # Bar chart: Titles on Y-axis, sales on X-axis

# Step 3 – Add labels and title
plt.title("Global Sales by Game (File 1)")
plt.xlabel("Game Title")
plt.ylabel("Global Sales (in millions)")

# Step 4 – Layout fix to prevent label cutoff
plt.tight_layout()

# Step 5 – Show the chart
plt.show()

genre_avg_sales = df.groupby('Genre')['Global_Sales'].mean()

plt.figure(figsize=(8, 5))
genre_avg_sales.sort_values().plot(kind='barh', title='Average Global Sales by Genre')

plt.xlabel("Global Sales (Millions)")
plt.tight_layout()
plt.show()


genre_region_sales = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()

# Plot regional totals per genre
genre_region_sales.plot(kind='bar', figsize=(10, 6))
plt.title("Regional Sales by Genre")
plt.ylabel("Total Sales (Millions)")
plt.xlabel("Genre")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
'''
Questions to Answer
1. How many games are in the dataset ?
2. What are the most common genres or platforms?
3. Which game had the highest global sales?
4. Are there any missing values in the dataset?
5. What is the average sales in North America?

6. Bonus Challenge (Optional)
   Try grouping the data by genre or platform and calculate
   the average global sales for each group.

   # Example: Average global sales by genre
     print(df.groupby('Genre')['Global_Sales'].mean())
OR
# Add a Pivot Table
     df.pivot_table(values='Global_Sales', index='Genre', columns='Platform', aggfunc='mean')
# Count unique values in a column
    df['Genre'].value_counts()
# Filter rows or columns based on a condition or function
    df.filter(items=['Title', 'Global_Sales'])
# Apply multiple aggregation functions at once
    df.agg({'NA_Sales': ['mean', 'max'], 'EU_Sales': ['sum']})
# Sort the DataFrame by one or more columns.
    df.sort_values(by='Global_Sales', ascending=False)
# Remove duplicate rows.
    df.drop_duplicates(subset='Title')
'''