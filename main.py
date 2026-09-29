def add_student(students):
    """Add a student and their score."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        score = float(input("Enter student score (0-100): "))

        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return

        students[name] = score
        print(f"{name} has been added successfully.")

    except ValueError:
        print("Please enter a valid number for the score.")


def view_students(students):
    """Display all students and their scores."""
    if not students:
        print("No students have been added yet.")
        return

    print("\n--- Student Scores ---")

    for name, score in students.items():
        print(f"{name}: {score:.2f}")


def search_student(students):
    """Search for a student by name."""
    if not students:
        print("No students have been added yet.")
        return

    name = input("Enter student name to search: ").strip()

    if name in students:
        print(f"{name}'s score: {students[name]:.2f}")
    else:
        print("Student not found.")


def calculate_average(students):
    """Calculate the average student score."""
    if not students:
        print("No students have been added yet.")
        return

    average = sum(students.values()) / len(students)

    print(f"Average score: {average:.2f}")


def highest_score(students):
    """Find and display the student with the highest score."""
    if not students:
        print("No students have been added yet.")
        return

    highest_student = max(students, key=students.get)
    highest = students[highest_student]

    print(f"Highest score: {highest_student} - {highest:.2f}")


def lowest_score(students):
    """Find and display the student with the lowest score."""
    if not students:
        print("No students have been added yet.")
        return

    lowest_student = min(students, key=students.get)
    lowest = students[lowest_student]

    print(f"Lowest score: {lowest_student} - {lowest:.2f}")


def main():
    """Main program."""
    students = {}

    while True:
        print("\n===== STUDENT SCORE TRACKER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average")
        print("5. Highest Score")
        print("6. Lowest Score")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            calculate_average(students)

        elif choice == "5":
            highest_score(students)

        elif choice == "6":
            lowest_score(students)

        elif choice == "7":
            print("Thank you for using Student Score Tracker.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()
