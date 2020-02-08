BASE_VAL = 10
BASE_EXP = 1.5
## Function to ask user input for magnitude
def get_magnitude(num):
 magnitude = float(input("Enter the magnitude of earthquake "+ str(num) +":"))
 while( magnitude < 1):
     magnitude = float(input("Enter the magnitude of earthquake" + str(num) +":"))
 return magnitude

## Compares the magnitudes
def compare_magnitude(magnitude1, magnitude2):
        difference = BASE_VAL **( BASE_EXP * (magnitude1 - magnitude2) )
        return difference

## Will run function again if wanted
def get_run_again() :
    rerun = int(input("Try again? Type 1 for Yes: ") )
    if (rerun == 1):
         return True
    else:
         return False

## Main Function
def main():
    ## Sets retry to true
    retry = True
    ## when retry is true loop will continue
    while(retry):
        magnitude1 = get_magnitude(1)
        magnitude2 = get_magnitude(2)
    ## Compares the difference between magnitude1 and magnitude2
        compare = compare_magnitude(magnitude1, magnitude2)
    
        compare2 = (1 / compare_magnitude(magnitude1, magnitude2) )
        if( magnitude1 > magnitude2 ):
            print("An earthquake of magnitude",magnitude1,"is", "{0:.1f}".format(compare),"times more powerful than an earthquake with of magnitude",magnitude2)
        elif (magnitude2 > magnitude1):
            print("An earthquake of magnitude",magnitude2,"is", "{0:.1f}".format(compare2),"times more powerful than an earthquake with of magnitude",magnitude1)
        retry = get_run_again()
        if( retry == False):
            print("Bye")
main()

