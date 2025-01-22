import pandas as pd


# Read the dataset

df = pd.read_csv('Housing.csv')

# Extract features and target variable
x = df[['area', 'bedrooms']].values.tolist()  # Removed 'age' column
y = (df['price'] / 1000).tolist()  # Convert prices to thousands

# Print the first few rows to verify
print(x[:5])
print(y[:5])

# """
# Sample housing data (simplified version of typical housing dataset)
# """

# # Sample data: [square_feet, bedrooms, age]
# X = [
#     [1400, 3, 10],
#     [1800, 4, 15],
#     [1100, 2, 5],




# """
# Sample housing data (simplified version of typical housing dataset)
# """

# # Sample data: [square_feet, bedrooms, age]
# X = [
#     [1400, 3, 10],
#     [1800, 4, 15],
#     [1100, 2, 5],
#     [2100, 4, 8],
#     [1600, 3, 12],
#     [2400, 4, 20],
#     [1300, 3, 7],
#     [1900, 3, 16],
#     [2200, 4, 3],
#     [1500, 3, 9],
# ]

# # House prices in thousands (e.g., 250 = $250,000)
# y = [250, 340, 190, 390, 280, 420, 230, 350, 400, 270]