def main():
    ## List contains Countries for Final Standing
    placings = ["United States","Sweden","Switzerland","Canada","Great Britain","Norway","South Korea","Japam","Italy","Denmark"]
    ## Place holder for user input
    user = ""
    ## Loops until user inputs quit
    while(user != "quit"):
        ## User inputs a country
        user = input('Please enter a country, or "quit": ')
        ## Loops up to the length of list
        for i in range(len(placings)):
            ## If input is the same as current index of list
            if user == placings[i]:
                ## Adds one to index since index starts at 0
                standing = i + 1
                ## If the standing is 3, 2, or 1
                if standing <= 3:
                    ## If standing is 3 = Bronze Medal
                    if standing == 3:
                        print(placings[i],"placed",standing,"(Bronze Medal)")
                    ## If Standing is 2 = Silver Medal
                    if standing == 2:
                        print(placings[i],"placed",standing,"(Silver Medal)")
                    ## If standing is 1 = Gold Medal
                    if standing == 1:
                        print(placings[i],"placed",standing,"(Gold Medal)")
                ## Instead of 3,2,or 1 standing = 4,5,6,7,8,9,10
                elif standing > 3 and standing <= 10:
                    print(placings[i],"placed",standing)
        ## If user input = quit then ends program
        if user == "quit":
            print("Bye")
            break
        ## If input is not any value of list
        if user not in placings:
            print(user,"did not complete.")

main()