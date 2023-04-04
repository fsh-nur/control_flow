# loops
# for loops and for each loops

# In Python just for loops that you can then specify how you want to loop

# Collections

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {
    1: {"name" : "Bronson",
        "money": "$0.05"},
    2: {"name" : "Masha",
        "money": "$3.66"},
    3: {"name" : "Roscoe",
        "money" : "$1.14"
    }
}

for item in dict_data.values():
    print(item)

for items in dict_data.values():
    print(items["money"])

for num in list_data:
    if num == 3:
        print("I found three!")
    elif num > 3:
        print("I've gone too far!")
    else:
        print("Too soon!")

# While loops

# While loop = monitors a condition

x = 0

while x < 10:
    print(f"It's working -> {x}")
    if x == 4:
        break

    x += 1 # incrementer - each time it goes through the loops, after this it adds 1 onto x

# using while loops to verify user input

# age = input("What is your age ")
#
# print(f"Your age is {age}")


user_prompt = True

while user_prompt:
    age = input("What is your age ? ")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your age in digits")

print(f"Your age is {age}")