import sys

while True:
    try:
        N = int(input("Ievadi skaitli N: "))
        break
    except ValueError:
        print("N jābūt skaitlim mēģini vēlreiz.")

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
