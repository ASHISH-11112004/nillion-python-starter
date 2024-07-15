from nada_dsl import *

def nada_main():

    # Define the parties involved
    department1 = Party(name="Department1")
    department2 = Party(name="Department2")

    # Input secret integers for Department1
    salary1 = SecretInteger(Input(name="salary1", party=department1))
    salary2 = SecretInteger(Input(name="salary2", party=department1))
    count1 = SecretInteger(Input(name="count1", party=department1))  # Number of employees in Department1

    # Input secret integers for Department2
    salary3 = SecretInteger(Input(name="salary3", party=department2))
    salary4 = SecretInteger(Input(name="salary4", party=department2))
    count2 = SecretInteger(Input(name="count2", party=department2))  # Number of employees in Department2

    # Calculate total salaries and counts
    total_salary1 = salary1 + salary2
    total_salary2 = salary3 + salary4
    total_count = count1 + count2

    # Calculate combined total salary
    combined_total_salary = total_salary1 + total_salary2

    # Calculate the average salary
    if total_count != 0:
        average_salary = combined_total_salary / total_count
    else:
        average_salary = SecretInteger(0)  # Handle division by zero

    # Return the outputs
    return [
        Output(average_salary, "average_salary_output", department1),
        Output(average_salary, "average_salary_output", department2)
    ]
