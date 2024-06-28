'''
    CS50001
    Lab 1
    Fall 2023
    Isabel Cuddihy
    Find total cost of owning and car
'''
def main():
    INSURANCE = 1600
    miles = int(input("How many miles per month do you drive? "))
    price_of_gas = float(input("What is the average price of a gallon of gas? "))
    miles_per_gallon = int(input("How many miles per gallon does your car get on average? "))
    total = (INSURANCE / 12) + (miles/miles_per_gallon * price_of_gas) + (miles * .005)
    print(f"You total expense per month is ${total:.2f}")
    
if __name__ == "__main__":
    main()
