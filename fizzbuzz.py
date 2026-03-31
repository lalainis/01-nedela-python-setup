import sys

if len(sys.argv) == 2:
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)
else:
    N = 100  # default value

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
else: i % 2 == 0 
    print("PAIR")   
