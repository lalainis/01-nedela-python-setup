import sys
import random

while True:
    user_input = input("Ievadi skaitli N (vai spied Enter priekš nejauša 10-25): ")
    if user_input == '':
        N = random.randint(10, 25)
        print(f"Izmanto nejaušu N: {N}")
        break
    else:
        try:
            N = int(user_input)
            break
        except ValueError:
            print("N jābūt veselam skaitlim. Mēģini vēlreiz.")

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        if i % 2 == 0:
            print("PAIR FizzBuzz")
        else:
            print("FizzBuzz")
    elif i % 3 == 0:
        if i % 2 == 0:
            print("PAIR Fizz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        if i % 2 == 0:
            print("PAIR Buzz")
        else:
            print("Buzz")
    else:
        if i % 2 == 0:
            print("PAIR")
        else:
            print(i)
