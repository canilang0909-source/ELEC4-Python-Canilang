# Full Name: Harold Canilang
# Section: IV-BSIT-A
# Activity Code: p1_grade_calculator
# Date: November 18, 2026


# Function para mag-enter ng grades
def enter_grades():
    grades = []
    subjects = ["Elec1", "Elec2", "Elec3"]

    # Ulitin hanggang valid ang grade na ma-enter
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter {subject} grade: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Invalid grade! Enter a number from 0 to 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return grades


# Function para kunin ang average
def compute_average(grades):
    return sum(grades) / len(grades)


# Function para kunin ung highest grade
def get_highest(grades):
    return max(grades)


# Function para kunin ung lowest grade
def get_lowest(grades):
    return min(grades)


# I-check kung PASSED or FAILED ang student
def determine_status(grades):
    return "PASSED" if compute_average(grades) >= 75 else "FAILED"


# Function para ipakita ung results
def view_results(grades):
    if not grades:
        print("\nPlease enter grades first.")
        return
    
    print("\n---Grade Result of Student---")
    print(f"Grades: {grades}")
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades)}")
    print(f"Lowest Grade: {get_lowest(grades)}")
    print(f"Status: {determine_status(grades)}")


# Main function para sa menu ng program
def main():
    grades = []

    while True:
        print("\n---Calculator of Grades---")
        print("[1] Enter Grades\n[2] View Results\n[3] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("\nGrades successfully entered!")
        elif choice == "2":
            view_results(grades)
        elif choice == "3":
            print("\nThank you for using the Grade Calculator!")
            break
        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")


# Run the program
main()



# A local variable is created inside a function and can only be used within that function. For example, grades inside enter_grades() is a local variable.
# A global variable is created outside all
# functions and can be accessed by different functions throughout
# the program. This program uses local variables instead of global
# variables by passing grades through parameters and return values.
