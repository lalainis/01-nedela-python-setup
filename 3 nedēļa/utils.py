def capitalize_first_letter(word):
    if not word:
        return word  # Return the original word if it's empty
    return word[0].upper() + word[1:]
print(capitalize_first_letter("world"))

def truncate(text, max_len=10):
    """Apgriež tekstu, saglabājot tikai pirmos max_len simbolus."""
    return text[:max_len]
print(truncate("Šis ir ļoti garš teksts, kas jātruncē.", 15))

def count_words(text):
    """Saskaita vārdus tekstā."""
    return len(text.split())
print(count_words("Šis ir piemērs, lai saskaitītu vārdus manā mājas darbā."))

def clamp(value, min_value, max_value):
    """Ierobežo vērtību starp min_value un max_value."""
    return max(min_value, min(value, max_value))
print(clamp(-5, 0, 10))

def clamp_list(values, min_value, max_value):
    """Ierobežo katru vērtību sarakstā starp min_value un max_value.
    
    args:
        num skaitis ko ierobežot :-6    
        min_value minimālā vērtība :0
        max_value maksimālā vērtība :12

    returns: int vai float ierobežotā vērtība
    """
    return [clamp(value, min_value, max_value) for value in values]
print(clamp_list([-5, 0, 5, 10, 15], 0, 10))

def is_prime(num):
    """Pārbauda, vai skaitlis ir pirmskaitlis."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
input_number = 8
print(f"Vai {input_number} ir pirmskaitlis? {is_prime(input_number)}")

def factorial(n):
    """Aprēķina faktoriālu skaitlim n.
    
    args:
        n skaitlis, kura faktoriālu aprēķināt : 6
    returns: int faktoriāla vērtība
    """
    if n < 0:
        raise ValueError("Faktoriāls nav definēts negatīviem skaitļiem.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = 6
print(f"{n} faktoriāls ir: {factorial(n)}")