word = "butelki"
for beer_run in range(99, 0, -1):
    print("{} {} piwa na scianie.".format(beer_run, word))
    print("{} {} piwa.".format(beer_run, word))
    print('Jedną weź\nPodaj w koło.')

    if beer_run == 1:
        print("Nie ma już wiecej butelek piwa na ścianie.")
    else:
        new_number = beer_run - 1
        if new_number == 1:
            word = 'butelka'
        print("{} {} piwa na scianie.".format(new_number, word))
    print()

