# program is to check whether the number is Armstrong number or not


def calculate_armstrong_sum(number):
    """
    Calculates the sum of each digit of a number raised to the power of
    the total number of digits in the number.
    """
    # Initializing sum and counting number of digits
    digit_sum = 0
    num_digits = 0

    # Count the number of digits
    temp_number = number
    while temp_number > 0:
        num_digits += 1
        temp_number //= 10

    # Calculate the Armstrong sum
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        digit_sum += digit**num_digits
        temp_number //= 10

    return digit_sum


# End of Function

# User Input
input_number = int(input("\nPlease enter the number to check for Armstrong: "))

# Check and display result
if input_number == calculate_armstrong_sum(input_number):
    print(f"\n{input_number} is an Armstrong number.\n")
else:
    print(f"\n{input_number} is not an Armstrong number.\n")
