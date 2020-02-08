## User Inputs Car Year and Price
car_price = float(input("Enter Original Car Price: ") )
while ( car_price <= 0 ):
    car_price = float(input("Enter Original Car Price: ") )
car_year = int(input("Enter Number Of Years: ") )
while( car_year <=0 ):
    car_year = int(input("Enter Number Of Years: ") )
## Iterates up to Car Year by 1
for i in range ( 1,car_year+1):
    depreciated_lost = .18 * car_price ## Calculates Depreciated Value
    depreciated_val = car_price - depreciated_lost
    car_price = depreciated_val ## Sets Car Price to new depreciated value
    print("Year", i , "value:", "${0:.2f}".format(depreciated_val))

