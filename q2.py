#/*****************************************************/
#/* CS03A - Summer 2026
#/* Assignment 1 - Question 2
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/
def run():
    """
    Students should implement their code for Question 2 inside this function.
    """
    # TODO: Write your code here
    month = int(input("Enter a month in numeric form: "))
    day = int(input("Enter a day in numeric form: "))
    year = int(input("Enter a two digit year: "))
    if month * day == year:
        print(f"Result: the date is magic")
    else:
        print("Result: The date is not magic")

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()