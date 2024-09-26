def sum_even_numbers(start, end):
    """Calculate the sum of even numbers in a given range."""
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:  # Check if the number is even
            total += number
    return total

def get_user_input():
    """Get valid start and end values from the user."""
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            if start > end:
                print("Start must be less than or equal to end. Please try again.")
                continue
            return start, end
        except ValueError:
            print("Invalid input. Please enter integer values.")

def main():
    """Main function to run the program."""
    while True:
        start, end = get_user_input()
        result = sum_even_numbers(start, end)
        print(f"The sum of even numbers from {start} to {end} is: {result}")

        # Ask if the user wants to continue
        continue_choice = input("Do you want to calculate another range? (yes/no): ").strip().lower()
        if continue_choice not in ['yes', 'y']:
            print("Thank you for using the program!")
            break

if __name__ == "__main__":
    main()
