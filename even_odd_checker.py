def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

user_input = input("Enter a number: ")
try:
    user_input = int(user_input)
    result = check_even_odd(user_input)
    print(f"The number {user_input} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")