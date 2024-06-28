'''
    CS50001
    Homework 01 - Electric Bill
    09-14-2023
    Isabel Cuddihy

    Calculate total monthly electric bill
'''
def main():
   
    supply_charge = float(input("What is the supplier fee per kWh ?"))
    power_delivery_charge = float(input("What is the power fee per kWH? "))
    kilowatt_hours = float(input("How many kWh were used this month? "))
    total_bill = (supply_charge * kilowatt_hours) + (
        power_delivery_charge * kilowatt_hours)
    print(f"Your electric bill this month is ${total_bill:.2f}")

if __name__ == "__main__":
    main()
