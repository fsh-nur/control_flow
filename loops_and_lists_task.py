# loop with a range that says hello 10 times

for i in range(1, 10):
    print("Hello")

# Create another loop with a range that asks for name and appends to list_names
list_names = []

for x in range(0, 5):
    name = input("What is your name? ")
    list_names.append(name)

# print(list_names)

# Make a loop that iterates over each name in list_name and formats it into lowercase in a new variable called
# list_names_lower

list_names_lower = []

for item in list_names:
    list_names_lower.append(item.lower())
print(list_names_lower)

# Iterate over the list of values to find out if they are even

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list_data:
    if num % 2 == 0:
        print(f"{num} is even")
