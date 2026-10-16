
students = []


def add_student():
    print("\n--- Add Student ---")

    student = {
        "name": input("Enter name: ").strip(),
        "roll": input("Enter roll number: ").strip(),
        "course": input("Enter course: ").strip(),
        "cgpa": input("Enter CGPA: ").strip(),
        "company": input("Enter company name: ").strip(),
        "status": input("Enter placement status: ").strip()
    }

    students.append(student)
    print("\nStudent added successfully!")


def view_students():
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        for key, value in student.items():
            print(f"{key.title()}: {value}")
        print("-" * 30)


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            for key, value in student.items():
                print(f"{key.title()}: {value}")
            return

    print("Student not found.")


def main():
    while True:
        print("\n==============================")
        print(" COLLEGE PLACEMENT MANAGEMENT")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
