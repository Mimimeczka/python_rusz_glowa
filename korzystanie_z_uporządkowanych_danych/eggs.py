phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)
plist.remove("P")
plist.remove("!")
plist.remove("a")
plist.remove("j")
plist.remove("k")
plist.pop(len(plist) - 1)
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

print()

phrase = "Podaj jajko!"
plist = list(phrase)
print(phrase)
print(plist)
plist = plist[1:3] + plist[5:9]
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)