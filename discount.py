# This function calculates a discount if the discount percent is 20% or more
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price (no discount)
        return price

# This is the main function that handles user input and displays the result
def main():
    # Ask the user to enter the original price of the item
    original_price = float(input("Enter the original price: "))
    
    # Ask the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Compare the final price with the original price to determine if a discount was applied
    if final_price != original_price:
        print("Discount applied. Final price: KSh {:.2f}".format(final_price))
    else:
        print("No discount. Final price: KSh {:.2f}".format(original_price))

# This line ensures that the main() function only runs when this script is executed directly
# It prevents the main() code from running if this file is imported into another Python file as a module
if __name__ == "__main__":
    main()
