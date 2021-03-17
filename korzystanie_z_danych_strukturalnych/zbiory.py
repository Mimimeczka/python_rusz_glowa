vowels = set('aeiouy') # tworzenie zbioru samogłosek
print(vowels)
word = 'kicaj'
suma = vowels.union(set(word)) # suma dwóch zbiorów
print('vowels', vowels)
print('word', word)
print("suma", suma)

word = input("Podaj zdanie w którym Python ma odszukać samogłoski: ")
found = vowels.intersection(set(word))
print(found)

people = {'Zaczyk': {'name': 'Justyna Zaczyk', 'mail': 'justyna.zaczyk@onet.pl', 'number': 734420071},
          'Slaby': {'name': 'Jaroslaw Slaby', 'mail': 'jaroslaw.slaby@gmail.pl', 'number': 764920382}}

print(people['Zaczyk']['number'])

import pprint

pprint.pprint(people)