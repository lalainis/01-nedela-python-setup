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