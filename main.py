# jls_extract_var = """
# Main script to train, test, and predict house prices using user input
# """
# jls_extract_var

from data import x, y
from linear_regression import LinearRegression

def main():
    # Update data to exclude the age feature
    x_no_age = [features[:2] for features in x]  # Only use square_feet and bedrooms
    
    # Extract ranges for validation
    square_feet_range = (min(f[0] for f in x_no_age), max(f[0] for f in x_no_age))
    bedrooms_range = (min(f[1] for f in x_no_age), max(f[1] for f in x_no_age))
    
    # Split data into training (80%) and testing (20%) sets
    split_idx = int(0.8 * len(x_no_age))
    X_train, X_test = x_no_age[:split_idx], x_no_age[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on test data
    predictions = model.predict(X_test)
    
    # Print results
    print("\nHouse Price Predictions:")
    print("------------------------")
    print("Format: [square_feet, bedrooms] => Predicted Price ($K) | Actual Price ($K)")
    for X_i, pred, actual in zip(X_test, predictions, y_test):
        print(f"{X_i} => ${pred:.1f}K | ${actual}K")
    
    # Calculate and print Mean Absolute Error
    mae = sum(abs(p - a) for p, a in zip(predictions, y_test)) / len(predictions)
    print(f"\nMean Absolute Error: ${mae:.1f}K")
    
    # User input for house features
    while True:
        print("\nEnter house details to predict price (or type 'exit' to quit):")
        user_input = input("Enter square_feet, bedrooms (comma-separated): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        
        try:
            square_feet, bedrooms = map(float, user_input.split(","))
            
            # Validate input ranges
            if not (square_feet_range[0] <= square_feet <= square_feet_range[1]):
                print(f"Error: square_feet must be between {square_feet_range[0]} and {square_feet_range[1]}.")
                continue
            if not (bedrooms_range[0] <= bedrooms <= bedrooms_range[1]):
                print(f"Error: bedrooms must be between {bedrooms_range[0]} and {bedrooms_range[1]}.")
                continue
            
            user_features = [[square_feet, bedrooms]]
            user_prediction = model.predict(user_features)[0]
            print(f"Predicted Price for [{square_feet}, {bedrooms}]: ${user_prediction:.1f}K")
        except ValueError:
            print("Invalid input. Please enter values in the format: square_feet, bedrooms")
from data import x, y
from linear_regression import LinearRegression

def main():
    # Update data to exclude the age feature
    x_no_age = [features[:2] for features in x]  # Only use square_feet and bedrooms
    
    # Extract ranges for validation
    square_feet_range = (min(f[0] for f in x_no_age), max(f[0] for f in x_no_age))
    bedrooms_range = (min(f[1] for f in x_no_age), max(f[1] for f in x_no_age))
    
    # Split data into training (80%) and testing (20%) sets
    split_idx = int(0.8 * len(x_no_age))
    X_train, X_test = x_no_age[:split_idx], x_no_age[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on test data
    predictions = model.predict(X_test)
    
    # Print results
    print("\nHouse Price Predictions:")
    print("------------------------")
    print("Format: [square_feet, bedrooms] => Predicted Price ($K) | Actual Price ($K)")
    for X_i, pred, actual in zip(X_test, predictions, y_test):
        print(f"{X_i} => ${pred:.1f}K | ${actual}K")
    
    # Calculate and print Mean Absolute Error
    mae = sum(abs(p - a) for p, a in zip(predictions, y_test)) / len(predictions)
    print(f"\nMean Absolute Error: ${mae:.1f}K")
    
    # User input for house features
    while True:
        print("\nEnter house details to predict price (or type 'exit' to quit):")
        user_input = input("Enter square_feet, bedrooms (comma-separated): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        
        try:
            square_feet, bedrooms = map(float, user_input.split(","))
            
            # Validate input ranges
            if not (square_feet_range[0] <= square_feet <= square_feet_range[1]):
                print(f"Error: square_feet must be between {square_feet_range[0]} and {square_feet_range[1]}.")
                continue
            if not (bedrooms_range[0] <= bedrooms <= bedrooms_range[1]):
                print(f"Error: bedrooms must be between {bedrooms_range[0]} and {bedrooms_range[1]}.")
                continue
            
            user_features = [[square_feet, bedrooms]]
            user_prediction = model.predict(user_features)[0]
            print(f"Predicted Price for [{square_feet}, {bedrooms}]: ${user_prediction:.1f}K")
        except ValueError:
            print("Invalid input. Please enter values in the format: square_feet, bedrooms")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()





# """
# Main script to train and test the house price prediction model
# """

# from data import x, y
# from linear_regression import LinearRegression

# def main():
#     # Split data into training (80%) and testing (20%) sets
#     split_idx = int(0.8 * len(x))
#     X_train, X_test = x[:split_idx], x[split_idx:]
#     y_train, y_test = y[:split_idx], y[split_idx:]
    
#     # Create and train the model
#     model = LinearRegression()
#     model.fit(X_train, y_train)
    
#     # Make predictions on test data
#     predictions = model.predict(X_test)
    
#     # Print results
#     print("\nHouse Price Predictions:")
#     print("------------------------")
#     print("Format: [square_feet, bedrooms, age] => Predicted Price ($K) | Actual Price ($K)")
#     for X_i, pred, actual in zip(X_test, predictions, y_test):
#         print(f"{X_i} => ${pred:.1f}K | ${actual}K")
    
#     # Calculate and print Mean Absolute Error
#     mae = sum(abs(p - a) for p, a in zip(predictions, y_test)) / len(predictions)
#     print(f"\nMean Absolute Error: ${mae:.1f}K")

# if __name__ == "__main__":
#     main()