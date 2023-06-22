import csv


def MAIN_menu():
    print("=============================================")
    print("       SIMPLE STUDENT AND COURSE SYSTEM     ")
    print("=============================================")
    print(" M  E  N  U")
    print("[1] CRUDL for Student data")
    print("[2] CRUDL for Course Codes")
    print("[3] Exit")


def STUDENT_menu():
    print("=============================================")
    print("            CRUDL for Student Data           ")
    print("=============================================")
    print("[1] Add Student")
    print("[2] View All Students")
    print("[3] Update Student")
    print("[4] Delete Student")
    print("[5] Search Student")
    print("[6] Back to the Main Menu")


def COURSE_menu():
    print("=============================================")
    print("             CRUDL for Course Code           ")
    print("=============================================")
    print("[1] Add Course")
    print("[2] View All Courses")
    print("[3] Update Course")
    print("[4] Delete Course")
    print("[5] Search Course")
    print("[6] Back to the Main Menu")

def add_student():
    print("          ADD STUDENT INFORMATION            ")

    ID_Number = input("Enter Student ID Number: ")
    Name = input("Enter Student Name: ")
    Gender = input("Enter Student Gender: ")
    Year_Level = input("Enter Student Year Level: ")
    Course_Code = input("Enter Student Course Code: ")

    # Check if the Course_Code exists in CourseData.csv
    with open('CourseData.csv', 'r') as course_file:
        reader = csv.reader(course_file)
        course_codes = [row[0] for row in reader]

    if Course_Code not in course_codes:
        print("Error: Course code does not exist. Student cannot be added.")
        input("Press Enter to Continue...")
        return

    with open('StudentData.csv', 'a', newline='') as file:
        student_data = csv.writer(file)
        student_data.writerow([ID_Number, Name, Gender, Year_Level, Course_Code])
        print("Student information added successfully")
        input("Press Enter to Continue...")


def view_all_students():
    print("       VIEW ALL STUDENTS INFORMATION       ")

    with open('StudentData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    input("Press Enter to Continue...")


def update_student():
    print("          EDIT STUDENT INFORMATION         ")

    rows = []
    with open('StudentData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    ID_Number = input("Enter the ID number of the student to edit: ")

    found = False
    for row in rows:
        if row[0] == ID_Number:
            found = True
            print("What would you like to edit?")
            print("[0] Id No.")
            print("[1] Name")
            print("[2] Age")
            print("[3] Year Level")
            print("[4] Course Code")
            choice = input("Enter your choice: ")

            if choice == '0':
                row[0] = input("Enter the edited ID NO..: ")
            elif choice == '1':
                row[1] = input("Enter the edited Name")
            elif choice == '2':
                row[2] = input("Enter the edited Age: ")
            elif choice == '3':
                row[3] = input("Enter the edited Year Level: ")
            elif choice == '4':
                row[4] = input("Enter the edited Course Code: ")
            else:
                print("Invalid choice. No changes made.")

            break

    if found:
        with open('StudentData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Student information updated successfully")
    else:
        print("Student with ID number", ID_Number, "not found")

    input("Press Enter to Continue...")


def delete_student():
    print("        DELETE STUDENT INFORMATION       ")

    with open('StudentData.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("No records found to delete")
        input("Press Enter to Continue...")
        return

    ID_Number = input("Enter the ID Number of the student to be deleted: ")

    found = False
    for i, row in enumerate(rows):
        if row[0] == ID_Number:
            found = True
            del rows[i]
            print("Student with ID Number {} deleted successfully".format(ID_Number))
            break

    else:
        print("Student not found")
        input("Press Enter to Continue...")
        return

    with open('StudentData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    input("Press Enter to Continue...")


def search_student():
    print("        SEARCH STUDENT INFORMATION         ")

    ID_Number = input("Enter the ID number of the student to search: ")
    found = False

    with open('StudentData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == ID_Number:
                found = True
                print(f"ID Number: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"Year: {row[3]}")
                print(f"Course Code: {row[4]}")
                break

    if not found:
        print("Student with ID number", ID_Number, "not found")

    input("Press Enter to Continue...")


def add_course():
    print("          ADD COURSE INFORMATION            ")

    Course_Code = input("Enter Course Code: ")
    Course_Name = input("Enter Course Name: ")

    with open('CourseData.csv', 'a', newline='') as file:
        course_data = csv.writer(file)
        course_data.writerow([Course_Code, Course_Name])
        print("Course information added successfully")
        input("Press Enter to Continue...")


def view_all_courses():
    print("       VIEW ALL COURSES INFORMATION       ")

    with open('CourseData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    input("Press Enter to Continue...")


def update_course():
    print("          EDIT COURSE INFORMATION         ")

    rows = []
    with open('CourseData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    Course_Code = input("Enter the Course Code to edit: ")

    found = False
    for row in rows:
        if row[0] == Course_Code:
            found = True
            row[0] = input("Enter the edited course code:")
            row[1] = input("Enter the edited course name: ")
            break

    if found:
        with open('CourseData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Course information updated successfully")
    else:
        print("Course with Course Code", Course_Code, "not found")

    input("Press Enter to Continue...")


def delete_course():
    print("        DELETE COURSE INFORMATION       ")

    Course_Code = input("Enter the Course Code to be deleted: ")

    students_to_delete = []

    with open('StudentData.csv', 'r') as student_file:
        student_reader = csv.reader(student_file)
        students = list(student_reader)

        for i, student_row in enumerate(students):
            if student_row[4] == Course_Code:
                students_to_delete.append(student_row)
                del students[i]

    if not students_to_delete:
        print("No students found with course code", Course_Code)
    else:
        with open('StudentData.csv', 'w', newline='') as student_file:
            student_writer = csv.writer(student_file)
            student_writer.writerows(students)
        print("Students with course code", Course_Code, "deleted successfully")

    # Delete the course code from 'CourseData.csv'
    courses = []
    with open('CourseData.csv', 'r') as course_file:
        course_reader = csv.reader(course_file)
        for course_row in course_reader:
            if course_row[0] != Course_Code:
                courses.append(course_row)

    with open('CourseData.csv', 'w', newline='') as course_file:
        course_writer = csv.writer(course_file)
        course_writer.writerows(courses)

    input("Press Enter to Continue...")


def search_course():
    print("        SEARCH COURSE INFORMATION         ")

    Course_Code = input("Enter the Course Code to search: ")
    found = False

    with open('CourseData.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == Course_Code:
                found = True
                print(f"Course Code: {row[0]}")
                print(f"Course Name: {row[1]}")

                break

    if not found:
        print("Course with Course Code", Course_Code, "not found")

    input("Press Enter to Continue...")


while True:
    MAIN_menu()

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            STUDENT_menu()
            student_choice = input("Enter your choice: ")

            if student_choice == '1':
                add_student()
            elif student_choice == '2':
                view_all_students()
            elif student_choice == '3':
                update_student()
            elif student_choice == '4':
                delete_student()
            elif student_choice == '5':
                search_student()
            elif student_choice == '6':
                break  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        while True:
            COURSE_menu()
            course_choice = input("Enter your choice: ")

            if course_choice == '1':
                add_course()
            elif course_choice == '2':
                view_all_courses()
            elif course_choice == '3':
                update_course()
            elif course_choice == '4':
                delete_course()
            elif course_choice == '5':
                search_course()
            elif course_choice == '6':
                break  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == '3':
        break  # Exit the program
    else:
        print("Invalid choice. Please try again.")
