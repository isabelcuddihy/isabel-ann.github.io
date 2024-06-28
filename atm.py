'''
    CS50001
    Homework 01 - ATM
    09-14-2023
    Isabel Cuddihy
    
    Input ATM withdrawl amount in dollars
    Output breakdown of bill types to receive largest to smallest (50-1)

    Test Case #1
    input = $23
    output = 0 fiftes, 1 twenties , 0 tens, 0 fives, 3 ones
    
    Test Case #2
    input = $135
    output = 2 fifties ,  1 twenties , 1 tens, 1 fives, 0 ones

    Test Case #3
    input = 86
    output = 1 fifties, 1 twenties, 1 tens, 1 fives, 1 ones
'''
def main():

    withdrawl_amount = int(input("Welcome to PDQ Bank! Amount to withdraw? $"))
    print(f"Cha - ching! You asked for ${withdrawl_amount}")
    fifties = withdrawl_amount // 50 
    twenties = (withdrawl_amount - (50 * fifties)) // 20
    tens = (withdrawl_amount - (50 * fifties) - (20 * twenties)) // 10
    fives = (withdrawl_amount - (50 * fifties) - (
        20 * twenties) - (10 * tens)) // 5
    ones = (withdrawl_amount - (50 * fifties) - (
        20 * twenties) - (10 * tens) - (5 * fives)) // 1
    print(f""" That breaks down to:
          {fifties} fifties
          {twenties} twenties
          {tens} tens
          {fives} fives
          {ones} ones

          """)

if __name__ == "__main__":
    main()
