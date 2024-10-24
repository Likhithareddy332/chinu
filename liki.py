# Function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

# Test the function
num = int(input("Enter a number: "))
if is_odd(num):
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number.")
