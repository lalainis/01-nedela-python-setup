import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
attempts = 0

print("Laipni lūgts skaitļu minēšanas spēlē!")
print("Es iedomājos skaitli no 1 līdz 100.")
print("Vai tu to vari uzminēt?")

while True:
    if attempts >= 10:
        print("Spēle beigusies! Tu neuzminēji skaitli 10 mēģinājumos.")
        print(f"Pareizais skaitlis bija {random_number}.")
        break
    
    try:
        guess = int(input("Ievadi savu minējumu: "))
        
        if guess < 1 or guess > 100:
            print("Lūdzu, ievadi skaitli no 1 līdz 100.")
            continue
        
        attempts += 1

        if guess < random_number:
            print("Pārāk mazs! Mēģini vēlreiz.")
        elif guess > random_number:
            print("Pārāk liels! Mēģini vēlreiz.")
        else:
            print(f"Apsveicu! Tu uzminēji {attempts} mēģinājumos.")
            break
    except ValueError:
        print("Lūdzu, ievadi derīgu skaitli.")
