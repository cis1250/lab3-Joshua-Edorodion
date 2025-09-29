# Ask the user for a positive number
def get_number():
    while True:
        num = input("How many Fibonacci numbers do you want? ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Please enter a positive number.")

# Print the Fibonacci sequence
def show_fibonacci(count):
    first = 0
    second = 1
    for _ in range(count):
        print(first, end=' ')
        next_num = first + second
        first = second
        second = next_num
    print()  # Move to the next line after printing

# Run the program
def run():
    total = get_number()
    show_fibonacci(total)

# Start the program only if this file is run directly
if __name__ == "__main__":
    run()
