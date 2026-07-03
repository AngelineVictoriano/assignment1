def run():
    """
    Students should implement their code for Question 4 inside this function.
    """
    # TODO: Write your code here

    base_tuition = 8000
    yearly_tuition = 0
    for i in range(5):
        if i == 0:
            yearly_tuition = base_tuition*1.03
        else:
            yearly_tuition = yearly_tuition*1.03
        print(f"Year {i+1} tuition: ${round(yearly_tuition, 2)}")

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()