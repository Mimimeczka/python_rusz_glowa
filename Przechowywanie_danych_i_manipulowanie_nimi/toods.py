toods = open('toods.txt', 'a')
print('aaaaaa', file=toods)
print('bbbbbb', file=toods)
print('cccccc', file=toods)
toods.close()