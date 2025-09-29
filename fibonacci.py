# Define a function to repeatedly prompt the user until they enter a valid positive integer
def get_positive_integer():
    while True:  # Loop continues until a valid input is received
        user_input = input("Enter the number of Fibonacci terms you want: ")  # Ask user for input
        # Check if input is a digit and greater than zero
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)  # Convert to integer and return it
        else:
            # If input is invalid (non-digit or zero/negative), show error and repeat
            print("Please enter a positive integer.")

# Define a function to generate and print the Fibonacci sequence
def generate_fibonacci(n):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(n):  # Loop n times to generate n terms
        print(a, end=' ')  # Print the current term followed by a space
        a, b = b, a + b  # Update a and b to the next pair in the sequence
    print()  # Print a newline after the sequence ends

# Main function to coordinate input and output
def main():
    num_terms = get_positive_integer()  # Get valid number of terms from user
    generate_fibonacci(num_terms)  # Generate and display the Fibonacci sequence

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
