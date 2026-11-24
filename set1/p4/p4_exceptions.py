# Full Name: Harold Canilang
# Section: IV-BSIT-A
# Activity Code: p4_exceptions
# Date: November 18, 2026


# Function para mag-divide ng dalawang numbers
def division():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b

    # Kapag hindi number ang input
    except ValueError:
        print("Invalid input! Please enter numbers.")

    # Kapag zero ung pangalawang number
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    # Kapag walang error, ipakita ung result
    else:
        print("Result:", result)

    # Laging magrurun ket may error o wala
    finally:
        print("Division operation finished.")


# Function para mag-open at magbasa ng file
def open_file():
    try:
        filename = input("Enter file name: ")

        with open(filename, "r") as file:
            print(file.read())

    # Kapag hindi makita ung file
    except FileNotFoundError:
        print("File not found!")

    # Laging magrurun pagkatapos ng file operation
    finally:
        print("File operation finished.")


# Main menu ng program
while True:
    print("\n---Exception Handling Menu---")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        division()
    elif choice == "2":
        open_file()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Choose only from 1 to 3!")
