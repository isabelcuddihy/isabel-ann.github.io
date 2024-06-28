'''
    CS50001
    Lab 0
    Fall 2023
    Isabel Cuddihy
'''
def main():
    '''
    Using office length and width measurements
    find square feet, square meters
    and the monthly cost in euros per square meter
    '''
    office_length = float(input("Enter the length of the office (in feet) "))
    office_width = float(input("Enter the width of the office (in feet) "))
    square_feet = office_length * office_width
    square_meters = square_feet * 0.092903
    euros_per_month = square_meters * 21.10
    print(f"The area of the office is {square_feet:.2f} square feet")
    print(f"...which is {square_meters:.2f} square meters")
    print(f"......and you will pay €{euros_per_month:.2f} per month")
if __name__== "__main__":
    main()
