## Function asks user to input a word and returns it
def get_word():
    ## User inputs a word assigned to variable word
    word = input("Please enter a word: ")
    ## returns the word when function is called
    return word

## Function that is given a letter will determine whether the letter is a vowel or a consonant
def is_vowel(letter):
    ## If letter is a, e, i ,o, or u the function will return true
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    ## if its something else other than a vowel the function will return false
    else:
        return False

## Function is given a word as a string, determines the measure of word
def calculate_measure(word):
    ## counter for measure
    measure = 0
    ## Creates a new variable which assigns true or false depending on the first letter of the word
    letter_before = is_vowel( word[0] )
    ## Creates a loop that iterates from 1 to the length of the word
    for i in range (1,len(word)):
        ## assigns letter to the function of is_vowel with the parameter of the index of i in word
        letter = is_vowel(word[i])
        ## if the first letter is true which is a vowel and the second is false which is a consonant
        if letter_before == True and letter == False:
            ## measure will increment by 1
            measure += 1
        ## assigns the current letter postion to the previous letter variable   
        letter_before = letter
    return measure

## Main function that calls every other function
def main():
    word = get_word()
    measure = calculate_measure(str(word))
    print(word, "has a measure of","{0:.0f}.".format(measure) )
    
main()
