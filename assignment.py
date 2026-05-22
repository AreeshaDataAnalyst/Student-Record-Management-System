# Student Record Management System

FILE_NAME = "student.txt"

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"
    
# Function to add student

def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter The Student Roll Number: ")
    marks = input("Enter The Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll_no},{marks}\n")

    print("Student record added successfully!\n")


# Function to view all students

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.\n")
                return

            print("\n--- Student Records ---")

            for line in records:
                name, roll_no, marks = line.strip().split(",")

                grade = calculate_grade(int(marks))

                print(
                    f"Name: {name} | Roll No: {roll_no} | Marks: {marks} | Grade: {grade}"
                )

            print(f"\nTotal Students: {len(records)}\n")

    except FileNotFoundError:
        print("File not found. No records available.\n")


# Function to search student
def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, roll_no, marks = line.strip().split(",")

                if name.lower() == search_name.lower():
                    grade = calculate_grade(int(marks))

                    print("\nStudent Found!")
                    print(
                        f"Name: {name} | Roll No: {roll_no} | Marks: {marks} | Grade: {grade}\n"
                    )

                    found = True
                    break

        if not found:
            print("Student not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


# Function to clear all records
def clear_records():
    confirm = input(
        "Are you sure you want to clear all records? (yes/no): "
    )

    if confirm.lower() == "yes":
        open(FILE_NAME, "w").close()
        print("All records cleared successfully!\n")
    else:
        print("Operation cancelled.\n")


# Main Program Loop
while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Clear All Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        clear_records()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.\n")

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"