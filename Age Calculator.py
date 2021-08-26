"""
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether
the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
"""

age = int(input("Enter Your Age or Year of Birth:- "))

if age > 1900:
    count = 0 # age is 0 here
    while count < 100:
        count = count + 1
        age = age + 1
    print(f"Your age will reach hundred at {age}")

elif age < 200:
    new_age = 2021 - age
    new_age = new_age + 100
    print(f"Your age will reach hundred at {new_age}")

elif age > 2021:
    print("You are not yet born")

elif age > 200 and age < 1900:
    print("You seem to be the oldest person alive")

else:
    print("Something Went Wrong!!!\n\t Try Again")