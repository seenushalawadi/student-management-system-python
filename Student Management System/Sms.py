# Dictionary to store student records
students = {}

# Function to add a new student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    # Store student details in dictionary
    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully")


# Function to display all students
def view_students():

    # Check if dictionary is empty
    if not students:
        print("No students found")
        return

    print("\nStudent Records")

    # Loop through dictionary
    for roll, data in students.items():
        print("Roll:", roll)
        print("Name:", data["name"])
        print("Marks:", data["marks"])
        print("-------------------")


# Function to update student details
def update_student():
    roll = input("Enter Roll Number to update: ")

    # Check if student exists
    if roll in students:

        name = input("Enter new name: ")
        marks = input("Enter new marks: ")

        students[roll]["name"] = name
        students[roll]["marks"] = marks

        print("Student updated successfully")

    else:
        print("Student not found")


# Function to delete a student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted")
    else:
        print("Student not found")


# Main program loop
while True:

    print("\n---- Student Management System ----")
    print("1 Add Student")
    print("2 View Students")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again")
