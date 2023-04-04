user_age = input("Enter your age:  ")
age = int(user_age)


def movie_ratings(age):
    if age >= 18:  # User is 18+
        print("The following movie ratings are available for you: U, PG, 12, 15, 18")
    elif age >= 15:  # User is 15 +
        print("The following movie ratings are available for you: U, PG, 12, 15")
    elif age < 12:  # User is younger than 12
        print("The following movie ratings are available for you: U ")
    elif age >= 12:  # User is 12+
        print("The following movie ratings are available for you: U, PG, 12")
    else:
        print("This is not a valid age")
