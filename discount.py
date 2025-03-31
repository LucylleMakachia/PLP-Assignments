# Define the function
def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Apply the discount and calculate the final price
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Use the function to calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {original_price:.2f}")
