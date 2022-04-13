import random
import sys
import time
from time import sleep

#Stats
lvl = 90
pow = 110
atk = 205
defe = 188

#Modifiers
targets = 1
weather = 1
badge = 1
critical = 1
rdm = random.uniform(0.85, 1)
stab = 1.5
type = 0.5
burn = 1

#Formula
mod = (targets*weather*badge*critical*rdm*stab*type*burn*1)
dmg = ((((((2 * lvl / 5) + 2) * pow) * (atk / defe))) / (50 + 2) * mod)

#Print
l1 = "CHARIZARD used FIRE BLAST!"
for q in l1:
    sys.stdout.write(q)
    sys.stdout.flush()
    time.sleep(0.03)
sleep(0.80)
l2 = "\nIt's not very effective..."
for w in l2:
    sys.stdout.write(w)
    sys.stdout.flush()
    time.sleep(0.03)
sleep(0.90)
print("\nCHARIZARD attack dealt",round(dmg), "damage to FERALIGATR")