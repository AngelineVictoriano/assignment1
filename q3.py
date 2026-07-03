#/*****************************************************/
#/* CS03A - Summer 2026
#/* Assignment 1 - Question 3
#/* Student Name: Angeline Victoriano
#/* SID: 20528831
## /***************************************************/
def run():
    """
    Students should implement their code for Question 3 inside this function.
    """
    # TODO: Write your code here
    seconds = int(input("Enter number of seconds: "))
    days = 0
    hours = 0
    minutes = 0
    if seconds >= 86400:
        days = int(seconds/86400)
        seconds = seconds % 86400

    if seconds >= 3600:
        hours = int(seconds/3600)
        seconds = seconds % 3600

    if seconds >= 60:
        minutes = int(seconds/60)
        seconds = seconds % 60

    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()