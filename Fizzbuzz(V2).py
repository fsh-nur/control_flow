# FizzBuzz - Write a program that prints numbers from 1 - 100 but for multiples of 3 print "Fizz" and for multiples
# of 5 print "Buzz". For multiples of 3 and 5 print "FizzBuzz

num = 1


def fizzbuzz(num):
    while num <= 100:
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

