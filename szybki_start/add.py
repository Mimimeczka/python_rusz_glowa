from datetime import datetime
import time
import random

for x in range(5):
    righ_this_numbre = datetime.today().second
    print(righ_this_numbre)
    if righ_this_numbre % 2 == 0:
        print("Sekunda parzysta")
    else:
        print('Sekunda nieparzysta')
    if x < 4:
        time.sleep(random.randint(0, 10))


import sys
print('nazwa systeemu operacyjnego: ', sys.platform)

