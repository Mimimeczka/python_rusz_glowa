def search_vowels(search: str) -> set:
    """Ta funkcja zwraca zbiór znalezionych samogłosek"""
    return set(search).intersection(set('aeiouy'))


def search_letters(search: str, letters: str) -> set:
    """Ta funkcja zwraca zbiór szukanych znaków"""
    return set(letters).intersection(set(search))


def search_letters_or_vowels(search: str, letters: str = 'aeiouy') -> set:
    """Ta funkcja zwraca zbiór szukanych znaków.
    Jeśli nie podamy drugiego argumentu to funkcja bedzie szukała samogłosek"""
    return set(letters).intersection(set(search))



