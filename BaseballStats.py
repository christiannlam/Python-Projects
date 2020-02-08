
## Variables of each user input
player_name = input("Enter the player's full name: ")
plate_app = int(input("Enter how many times the player takes a turn at batting: "))
at_bats = int(input('How many At Bats: '))
num_walks = int(input('How many walks: '))
num_singles = int(input('How many singles: '))
num_doubles = int(input('How many doubles: '))
num_triples = int(input('How many triples: '))
num_homeruns = int(input('How many homeruns: '))

## Calculates the total amount of hits and prints
total_hits = num_singles + num_doubles + num_triples + num_homeruns
print("The player's total number of hits: ", end = " ")
print(total_hits)

## Calculates the batting average and prints
bat_avg = total_hits / at_bats
print("The player's batting average is:", "{0: .3f}".format(bat_avg))

## New Variables To Count Each Base
singles = num_singles * 1
doubles = num_doubles * 2
triples = num_triples * 3
homeruns = num_homeruns * 4

## Calculating total of bases earned
total_bases = singles + doubles + triples + homeruns
slug_per = total_bases / at_bats
print(" The player's slugging percentage is:","{0: .3f}".format(slug_per))

## Calculating the OBP
on_base_num = (total_hits + num_walks )
obp = on_base_num / plate_app

## Calculating the OPS
ops = obp + slug_per
print("The OPS is:","{0: .3f}".format(ops))

## Prints all values in simple form
print("\n",player_name, "had:\n",
             total_hits, " hits\n",
             "{0:.3f}".format(bat_avg), " AVG\n",
              "{0:.3f}".format(slug_per), " SLG\n",
              "{0:.3f}".format(ops), "OPS\n")
         

