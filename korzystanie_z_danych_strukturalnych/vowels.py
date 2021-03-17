word = input("Podaj tekst w którym Python ma sprawdzić liczbe samogłosek: ")
vowels = {}

for x in word:
    if x in "aeiouy":
        vowels.setdefault(x, 0)
        vowels[x] += 1

for key, value in sorted(vowels.items()):
    print(key, "-", value)


