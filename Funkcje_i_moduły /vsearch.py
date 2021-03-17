def search_vowels(search: str) -> set:
    '''Ta funkcja zwraca zbiór znalezionych samogłosek'''
    return set(search).intersection(set('aeiouy'))


print(search_vowels(input("Podaj ciąg znaków:")))


def search_letters(search: str, letters: str) -> set:
    '''Ta funkcja zwraca zbiór szukanych znaków'''
    return set(search).intersection(set(letters))


print(search_letters(input("Podaj ciąg znaków:"), input("Jakich znaków szukać: ")))


def search_letters_or_vowels(search: str, letters: str = 'aeiouy') -> set:
    '''Ta funkcja zwraca zbiór szukanych znaków.
    Jeśli nie podamy drugiego argumentu to funkcja bedzie szukała samogłosek'''
    return set(search).intersection(set(letters))


print(search_letters_or_vowels(input("Podaj ciąg znaków:"), input("Jakich znaków szukać: ")))
print(search_letters_or_vowels(input("Podaj ciąg znaków:"), input("Jakich znaków szukać: ")))
print(search_letters_or_vowels(input("Podaj ciąg znaków:")))
