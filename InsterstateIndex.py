## Function asks a user to input number that is positive
def get_interstate_number():
    interstate = input("Please enter a US Interstate Highway route number: ")

    if(interstate.startswith("Interstate")):
        interstate = int(interstate[11:])
    elif(interstate[0:2] == "I-"):
        interstate = int(interstate[2:])
    elif(interstate[0] == "I"):
        interstate = int(interstate[1:])
    else:
        interstate = int(interstate)

        ## Loops again if negative number is entered
    while (interstate < 0):
        interstate = input("Please enter a US Interstate Highway route number: ")

    return interstate

## Function returns true if number is single or double digit
def is_primary(number):
    if(1 <= number <= 99 ):
        return True
    ## Returns false if triple digit
    elif(number <= 100):
        return False

## Function determines the compass direction
def compass_orientation(number):
    ## if the number is odd
    if(number % 2 == 1):
        return "north-south"
    ## if number is even
    elif(number % 2 == 0):
        return "east-west"

## Function returns True or False
def is_arterial(number):
    ## if number is multiple of 5 returns True
    if(number % 5 == 0):
        return True
    else:
        return False

## Function returns radial or spur
def auxiliary_type(number):
    ## Trunks the number to leave first digit
    number = number // 100
    ## if first digit is even
    if(number % 2 == 0):
        return "radial"
    ## if first digit is odd
    elif(number % 2 == 1):
        return "spur"

## Function returns parent number
def parent_highway(number):
    ## Takes last two digits of number
    parent = number % 100
    return parent

def main():
    ## Creates new variables
    highway = get_interstate_number()
    orientation = compass_orientation(highway)
    aux_type = auxiliary_type(highway)
    parent = parent_highway(highway)

    if(is_primary(highway) == True):
        if(is_arterial(highway) == True):
            print("Interstate",highway,"is a long-distance arterial highway oriented","{}.".format(orientation))
        else:
            print("Interstate",highway,"is orientated","{}.".format(orientation))

    else:
        print("Interstate",highway,"is a",aux_type,"highway of Interstate","{}.".format(str(parent)))

main()