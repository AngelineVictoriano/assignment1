#/*****************************************************/
#/* CS03A - Summer 2026
#/* Assignment 1 - Question 1
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/
def run():
    """
    Students should implement their code for Question 1 inside this function.
    """
    # TODO: Write your code here
    prin = int(input("Enter the Principal Amount: "))
    rate = int(input("Enter interest rate: "))
    num_compound = int(input("Enter the number of times per year that the interest is compounded: "))
    num_years = int(input("Enter number of years the account will be left to earn interest: "))

    amt_money = prin * ((1 + rate/num_compound) ** (num_compound * num_years))
    print(f"Result: ${round(amt_money, 2)}")

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()