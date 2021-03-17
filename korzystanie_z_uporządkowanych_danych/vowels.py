vowels = ["a", "e", "i", "u", "o", "y"]
word = input("Podaj słowo/zdanie, w którym Python ma odszukać samogłoski:")
vowels_in_word = set()
for w in word:
    if w in "aeiouy":
        vowels_in_word.add(w)
print(vowels_in_word)
