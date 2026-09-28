class Student:

    def __init__(self, name, student_id, marks):
        self.name = name
        self.__student_id = student_id
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            return True
        else:
            return False

    def display(self):
        print("Name:", self.name)
        print("Student ID:", self.__student_id)
        print("Marks:", self.__marks)


students = []


def add_student():
    name = input("Enter name: ")
    student_id = input("Enter student ID: ")
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    student = Student(name, student_id, marks)
    students.append(student)

    print("Student added successfully")


def view_students():
    if len(students) == 0:
        print("No students available")
    else:
        for student in students:
            student.display()
            print()


def search_student():
    student_id = input("Enter student ID: ")

    for student in students:
        if student.get_student_id() == student_id:
            student.display()
            return

    print("Student not found")


def update_student():
    student_id = input("Enter student ID: ")

    for student in students:
        if student.get_student_id() == student_id:

            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))

            student.name = name

            if student.set_marks(marks):
                print("Student updated successfully")
            else:
                print("Invalid marks")

            return

    print("Student not found")


def delete_student():
    student_id = input("Enter student ID: ")

    for student in students:
        if student.get_student_id() == student_id:
            students.remove(student)
            print("Student deleted successfully")
            return

    print("Student not found")


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program ended")
        break

    else:
        print("Invalid choice")