import datetime

def calculate_year_of_100th_birthday(name, age):
    now = datetime.datetime.now()
    current_year = now.year
    years_to_100 = 100 - age
    year_of_100th_birthday = current_year + years_to_100
    return f"{name}, you will turn 100 years old in the year {year_of_100th_birthday}. You will be {age + years_to_100} years old in that year."

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(calculate_year_of_100th_birthday(name, age))