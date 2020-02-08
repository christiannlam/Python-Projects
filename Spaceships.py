import math
## CONSTANT VALUES USED
LIGHT_SPEED = 299792458
WARP_EXP = 10/3
ULA_RATE = 14830
SPACE_RATE = 2720
DAYS_YEAR = 365
SECONDS_DAY=86400
LIGHTS_INTO_METERS = 9460730472580800
## Creates Main Menu
## While Loop For Main Menu Function
def main_menu():
        print("\nMain Menu: (Enter 1-4)")
        print(" 1. Warp Speed\n",
                "2. Cost to Launch\n",
                "3. Time Dilation\n",
                "4. Quit")
        func = int(input("Select a Function: " ) )
        while( func < 1 or func > 4):
             func = int(input("Select a Function: " ) )
## Calculates Function 1
        if( func == 1 ):
            warp = float(input("Enter Warp Factor:  ") )
            while ( warp < 1 ):
                warp = float(input("Enter Warp Factor:  ") )
    ## Calculates the warp speed
            ship_speed = warp**(WARP_EXP) * LIGHT_SPEED
            print("Warp Factor:", "{0:,.0f}".format(warp))
            print("Warp","{0:,.0f},".format(warp),"engage!")
            print("You are now traveling at","{0:,.2f}".format(ship_speed),"meters per second.")
            main_menu()
## Calculates Function 2
        elif( func == 2):
            mass = float(input("Enter satellite mass in kilograms: ") )
            while ( mass<= 0):
                mass = float(input("Enter satellite mass in kilograms: ") )
            cost = float(input("Enter satellite cost in dollars: ") )
            while( cost <= 0 ):
                cost = float(input("Enter satellite cost in dollars: ") )
    ## Constant Value of insurance for SpaceX
            insurance = .30 * cost
    ## Calculates ULA price
            ula =  ULA_RATE * mass
    ## Calculates SpaceX price
            spcx = SPACE_RATE* mass + insurance
    ## Prints which company is cheaper
            if( ula > spcx ):
                save1 = ula - spcx
                print("SpaceX will save you", "${0:,.2f}".format(save1),"on this launch.")
                main_menu()
            if( spcx > ula ):
                save2 = spcx - ula
                print("United Launch Alliance will save you","${0:,.2f}".format(save2),"on this launch.")
                main_menu()
## Calculates Function 3
        elif (func== 3):
            user_distance = float(input("Enter travel distance in light years: " ) )
            while( user_distance <= 0):
               user_distance = float(input("Enter travel distance in light years: " ) )
            user_speed = float(input("Enter space ship velocity as a fraction of the speed of light: ") )
            while ( user_speed <=0 or user_speed >= 1 ):
                user_speed = float(input("Enter space ship velocity as a fraction of the speed of light: ") )
    ## Calculates speed into meters per second    
            user_speed = user_speed * LIGHT_SPEED
    ## Calculates time on earth in days
            earth_time = ( ( user_distance * LIGHTS_INTO_METERS) / user_speed ) / (SECONDS_DAY)
    ## Calculates time on spaceship in days
            dilation =  math.sqrt( 1 - ( (user_speed**2) / (LIGHT_SPEED**2) ) ) * earth_time
    ## Calculates the time on earth into years
            earth_years = math.floor(earth_time / DAYS_YEAR)
    ## Calculates the time on earth into days
            earth_days = earth_time % DAYS_YEAR
    ## Calculates the time on spaceship into years
            ship_years = math.floor(dilation / DAYS_YEAR)
    ## Calculates the time on spaceship into days
            ship_days = dilation % DAYS_YEAR

    ## Prints correct format when there is 1 or more years and when there is no years.
            if (earth_years > 1):
                print("An observer on Earth ages","{0:,.0f}".format(earth_years),"years,","{0:,.0f}".format(earth_days),"days during the trip")
            elif (earth_years == 1 ):
                print("An observer on Earth ages","{0:,.0f}".format(earth_years),"year,","{0:,.0f}".format(earth_days),"days during the trip")
            else:
                print("An observer on Earth ages","{0:,.0f}".format(earth_days),"days during the trip")

            if(ship_years > 1):
                print("A passenger on the ship ages","{0:,.0f}".format(ship_years),"years,","{0:,.0f}".format(ship_days),"days during the trip")
                main_menu()
            elif(ship_years == 1):
                 print("A passenger on the ship ages","{0:,.0f}".format(ship_years),"year,","{0:,.0f}".format(ship_days),"days during the trip")
                 main_menu()
            else:
                print("A passenger on the ship ages","{0:,.0f}".format(ship_days),"days during the trip")
                main_menu()

## Function 4: Ends Program
        elif( func== 4):
            print("You have terminated the program")
        
main_menu()    
