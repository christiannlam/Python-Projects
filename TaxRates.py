#User Inputs Income
income = int(input("What is your 2018 taxable income?: "))

#Calculating Tax liability and Effective Tax Rate

## Calculates the tax liability and rate for 10 percent
if (income >= 0 and income <= 9525 ):
      tax_liability = income * .10
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 12 percent      
elif ( income >= 9526 and income <= 38700 ):
      tax_liability =( 9525 * .10 ) + (.12 * ( income - 9525) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 22 percent
elif ( income >= 38701 and income <=  82500):
      tax_liability = (4453.5 + (.22 *  ( income - 38700 ) ) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 24 percent
elif ( income >= 82501 and income <=  157500):
      tax_liability = (14089.5 + (.24 * (income - 82500 ) ) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 32 percent
elif ( income >= 157501 and income <=  200000):
      tax_liability = (32089.5 + (.32 * ( income - 157500 ) ) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 35 percent
elif ( income >= 200001 and income <=  500000):
      tax_liability = (45689.5 + (.35 * ( income  - 200000) ) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

##  Calculates the tax liability and rate for 37 percent
elif ( income >= 500001 ):
      tax_liability = (150689.5 + (.37 *( income - 500000) ) )
      tax_rate = (tax_liability / income) * 100
      print("Your tax liability is","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate is","{0:.1f}%".format(tax_rate))

## Calculates the tax liability and rate for 70 percent
if( income >= 10000000 ):
      new_tax = 150689.5 + (.37 * 9500000 )
      tax_liability = new_tax + (.7 * (income - 10000000) ) 
      tax_rate = (tax_liability / income) * 100
      print("\nWith a new 70% bracket, your tax liability would be","${0:.2f}".format(tax_liability))
      print("Your effictive tax rate with the new bracket would be","{0:.1f}%".format(tax_rate))
