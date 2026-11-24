# Full Name: Harold Canilang
# Section: IV-BSIT-A
# Activity Code: p3_record_manager
# Date: November 18, 2026


# Set kung saan ise-save ung mga student names
students = set()


# Function para magdagdag ng student
def add_student():
    name = input("Enter student name: ").strip().lower()

    if name in students:
        print("Student already exists!")
    else:
        students.add(name)
        print("Student added!")


# Function para magtanggal ng student
def remove_student():
    name = input("Enter name to remove: ").strip().lower()

    if name in students:
        students.remove(name)
        print("Student removed!")
    else:
        print("Student not found!")


# Function para maghanap ng student
def search_student():
    name = input("Enter name to search: ").strip().lower()

    found = False

    # Hanapin kung may pangalan na nagmamatch sa search
    for student in sorted(students):
        if name in student:
            print(student.title())
            found = True

    if not found:
        print("Student not found!")


# Function para ipakita lahat ng students
def display_students():
    names = sorted(students)

    if not names:
        print("No students found!")
    else:
        # Ipakita ang names kasama ang kanilang number
        for i, name in enumerate(names, 1):
            print(f"{i}. {name.title()}")

        print("Total Students:", len(names))


# Main function para sa menu ng program
def main():
    while True:
        print("\n---Manager's Student Record---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please choose only from 1 to 5")


# Run the program
main()



# A list can contain duplicate values, while a set only stores unique values.
# I used a set to store student names and prevent duplicate entries.
# I used a list when searching for students and collecting the matching names.