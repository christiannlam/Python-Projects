import EnglishDictionary
import math

## Creates a function to print main menu
def print_menu():
    print("Main menu: ")
    print("1. Is it a palindrome?")
    print("2. Is it a crossword square?")
    print("3. Quit." )

## Function allows user to choose an option
def get_menu_choice():
    user = int(input("Choose a function: "))
    ## Loops until user inputs 1 2 or 3
    while( user < 0 and user > 4 ):
        user = int(input("Choose a function: "))
    return user

## Function asks user for a phrase
def get_phrase():
    phrase = str(input("Enter a phrase: "))
    ## Validates the phrase has at least one character if not it will loop
    while phrase == "":
        phrase = str(input("Enter a phrase: "))
    return phrase

## Function determines if it a palindrome
def is_palindrome(phrase):
    ## Sets the phrase to all lower cases
    phrase_lower = phrase.lower()
    i = 0
    j = len(phrase_lower)-1
    # Loops until i is greater than len(phrase)-1
    while i < j:
        ## Loop will increment i when not letter
        while( not phrase_lower[i].isalpha()):
            i+=1
        ## Loop will increment j when not a letter
        while( not phrase_lower[j].isalpha()):
            j-=1
        ## Returns false if one of the indexs do not match
        if (phrase_lower[i] != phrase_lower[j]):
            return False
        else:
            i+=1
            j-=1
    return True

## Function that outputs result of palindrome
def menu_check_palindrome():
    ## Calls the function get_phrase()
    phrase = get_phrase()
    ## If is_palindrome is true then it will print it is a palindrome
    if is_palindrome(phrase):
        print('"{}"'.format(phrase),"is a palindrome!")
    else:
        print('"{}"'.format(phrase),"is not a palindrome")

## Function asks the user to input set of words that form a crossword
def get_crossword_square():
    first_line = input("Please enter the first word of the square: ")
    ## Total variable to concatenate the strings
    string_total = first_line
    ## Loops until there are the same amount of words to the amount of indexes in the first word
    for i in range(len(first_line)-1):
        other_lines = input("Please enter the next word of the square: ")
        if(len(other_lines)!= len(first_line)):
            print("Lengths of words must match. Try another word")
            other_lines = input("Please enter the next word of the square: ")
        else:
            string_total += other_lines
    return string_total

## Function checks if the words pass as a crossword
def check_crossword_square(square):
    square = square.lower()
    ## Variable for the order of square
    n = int(math.sqrt(len(square)))
    ##Loops the concatenated string from left to right
    for i in range(n):
        ## Indexes by n each time
        row = square[(n * i):n + (n * i)]
        ## Determines if its an English Word
        if EnglishDictionary.is_word(row) == False:
            return False
        ##Loops the words from top to bottom
        for j in range(n):
            ## Indexes from top to bottom
            column = square[j * n + i]
            if EnglishDictionary.is_word(column) == False:
                return False
    return True

## Menu that outputs if the words create a crossword square
def menu_check_crossword_square():
    ## Creates words for crossword square
    word = get_crossword_square()
    ## Return True if words create a legal crossword
    result = check_crossword_square(word)
    ## Variable for order square
    n = int(math.sqrt(len(word)))
    ## Loop for rows of words
    for i in range(n):
        ## Variable to hold words in row format
        across = word[n*i:n+(n*i)]
        print(across)
    if(result == True):
        print("is a crossword square!")
    else:
        print("is not a crossword square")
## Main function that calls the other functions
def main():
    ## Default is true so it creates a continuous loop
    while(True):
        print_menu()
        option = get_menu_choice()
        ## If input is 1 function is called
        if(option == 1):
            menu_check_palindrome()
        elif (option == 2):
            menu_check_crossword_square()
        ## if input is 3 the option breaks the loop
        elif (option == 3):
            print("Bye!")
            break

main()












