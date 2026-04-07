def capitalize_first_letter(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    """
    Capitalizes the first letter of a word.
    
    Args:
        word (str): The word to capitalize.
    
    Returns:
        str: The word with the first letter capitalized.
    
    Example:
        >>> capitalize_first_letter("world")
        'World'
    """
    if not word:
        return word  # Return the original word if it's empty
    return word[0].upper() + word[1:]

def truncate(text, max_len=10):
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("max_len must be a non-negative integer.")
    """
    Truncates text, keeping only the first max_len characters.
    
    Args:
        text (str): The text to truncate.
        max_len (int, optional): Maximum number of characters to keep. Default is 10.
    
    Returns:
        str: The truncated text.
    
    Example:
        >>> truncate("Hello, world!", 5)
        'Hello'
    """
    return text[:max_len]

def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")
    """
    Counts the number of words in a text.
    
    Args:
        text (str): The text to count words in.
    
    Returns:
        int: The number of words in the text.
    
    Example:
        >>> count_words("This is a test.")
        4
    """
    return len(text.split())

def clamp(value, min_value, max_value):
    if not (isinstance(value, (int, float)) and isinstance(min_value, (int, float)) and isinstance(max_value, (int, float))):
        raise TypeError("All arguments must be int or float.")
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value.")
    """
    Clamps a value between min_value and max_value.
    
    Args:
        value (int or float): The value to clamp.
        min_value (int or float): The minimum allowed value.
        max_value (int or float): The maximum allowed value.
    
    Returns:
        int or float: The clamped value.
    
    Example:
        >>> clamp(15, 0, 10)
        10
    """
    return max(min_value, min(value, max_value))

def clamp_list(values, min_value, max_value):
    if not isinstance(values, (list, tuple)):
        raise TypeError("values must be a list or tuple.")
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError("All elements in values must be int or float.")
    if not (isinstance(min_value, (int, float)) and isinstance(max_value, (int, float))):
        raise TypeError("min_value and max_value must be int or float.")
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value.")
    """
    Clamps each value in a list between min_value and max_value.
    
    Args:
        values (list of int or float): The values to clamp.
        min_value (int or float): The minimum allowed value.
        max_value (int or float): The maximum allowed value.
    
    Returns:
        list of int or float: The clamped values.
    
    Example:
        >>> clamp_list([-5, 0, 5, 10, 15], 0, 10)
        [0, 0, 5, 10, 10]
    """
    return [clamp(value, min_value, max_value) for value in values]

def is_prime(num):
    if not isinstance(num, int):
        raise TypeError("num must be an integer.")
    """
    Checks if a number is a prime number.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Example:
        >>> is_prime(7)
        True
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    """
    Calculates the factorial of n.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial value.
    
    Example:
        >>> factorial(5)
        120
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

def total (numbers):
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("numbers must be a list or tuple.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in numbers must be int or float.")
    """
    Calculates the sum of numbers in a list.
    
    Args:
        numbers (list of int or float): The numbers to sum.
    
    Returns:
        int or float: The sum of the numbers.
    
    Example:
        >>> total([1, 2, 3, 4])
        10
    """
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

def average(numbers):
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("numbers must be a list or tuple.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in numbers must be int or float.")
    """
    Calculates the average value of numbers in a list.
    
    Args:
        numbers (list of int or float): The numbers to average.
    
    Returns:
        float: The average value. Returns 0 for an empty list.
    
    Example:
        >>> average([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        return 0  # Return 0 for an empty list to avoid division by zero
    total_sum = total(numbers)
    return total_sum / len(numbers)


if __name__ == "__main__":
    print(capitalize_first_letter("world"))
    print(truncate("Šis ir ļoti garš teksts, kas jātruncē.", 15))
    print(count_words("Šis ir piemērs, lai saskaitītu vārdus manā mājas darbā."))
    print(clamp(-5, 0, 10))
    print(clamp_list([-5, 0, 5, 10, 15], 0, 10))
    input_number = 8
    print(f"Vai {input_number} ir pirmskaitlis? {is_prime(input_number)}")
    n = 6
    print(f"{n} faktoriāls ir: {factorial(n)}")
    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))