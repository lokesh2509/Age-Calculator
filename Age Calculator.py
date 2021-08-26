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
