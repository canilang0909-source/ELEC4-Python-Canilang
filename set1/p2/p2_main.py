# Full Name: Harold Canilang
# Section: IV-BSIT-A
# Activity Code: p2_main
# Date: November 18, 2026


# Import ung functions mula sa student_utils
import student_utils
from student_utils import calculate_average
from datetime import datetime

# List kung saan ilalagay ung grades
grades = []

# Mga subjects na need lagyan ng grade
subjects = ["Elec1", "Elec2", "Elec3"]

# Kunin ung grade ng bawat subject
for subject in subjects:
    grade = float(input(f"Enter {subject} grade: "))
    grades.append(grade)

# Kunin ung average at iba pang results
average = calculate_average(grades)
result = student_utils.determine_pass_fail(average)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)

# Ipakita ung grade report
print("\n ---Grade Report of Student--- ")
print("Grades:", grades)
print("Average:", round(average, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", result)

# Ipakita ung date at time kung kailan ginawa ung report
print("\nReport Generated:", datetime.now().strftime("%B %d, %Y - %I:%M %p"))


#local variable is created inside the function which is ung enter_grades
#global variable is created outside of each functions
#kunwari sa classroom. I have my personal notebook which is me can only access to that notebook. that is local variable while ung global variable let say ung white board, everyone can access to that.
