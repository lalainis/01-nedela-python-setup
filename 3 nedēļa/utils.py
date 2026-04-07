def capitalize_first_letter(word):
    if not word:
        return word  # Return the original word if it's empty
    return word[0].upper() + word[1:]
print(capitalize_first_letter("world"))

def truncate(text, max_len=10):
    """Truncē tekstu, saglabājot tikai pirmos max_len simbolus."""
    return text[:max_len]
print(truncate("Šis ir ļoti garš teksts, kas jātruncē.", 15))

def count_words(text):
    """Saskaita vārdus tekstā."""
    return len(text.split())
print(count_words("Šis ir piemērs, lai saskaitītu vārdus manā mājas darbā."))
