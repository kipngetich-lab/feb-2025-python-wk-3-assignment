# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Check if a discount was applied and display the result
    if discount_percentage >= 20:
        print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: {original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")