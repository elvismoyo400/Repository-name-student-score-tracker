def main():
    students = {}

    print("Welcome to the Student Score Tracker!")

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average")
        print("5. Highest Score")
        print("6. Lowest Score")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        # Add Student
        if choice == "1":
            name = input("Enter student name: ").strip()

            if not name:
                print("Student name cannot be empty.")
                continue

            try:
                score = float(input("Enter student score: "))

                if score < 0 or score > 100:
                    print("Score must be between 0 and 100.")
                    continue

                students[name] = score
                print(f"Added {name} with score {score}.")

            except ValueError:
                print("Invalid score. Please enter a number.")

        # View Students
        elif choice == "2":
            if not students:
                print("No students recorded yet.")
            else:
                print("\nList of Students:")

                for name, score in students.items():
                    print(f"- {name}: {score}")

        # Search Student
        elif choice == "3":
            name = input("Enter student name to search: ").strip()

            if name in students:
                print(f"{name}'s score: {students[name]}")
            else:
                print("Student not found.")

        # Calculate Average
        elif choice == "4":
            if not students:
                print("No scores available to calculate average.")
            else:
                average = sum(students.values()) / len(students)
                print(f"Average score: {average:.2f}")

        # Highest Score
        elif choice == "5":
            if not students:
                print("No students recorded yet.")
            else:
                highest_student = max(students, key=students.get)
                highest_score = students[highest_student]

                print(f"Highest score: {highest_student} - {highest_score}")

        # Lowest Score
        elif choice == "6":
            if not students:
                print("No students recorded yet.")
            else:
                lowest_student = min(students, key=students.get)
                lowest_score = students[lowest_student]

                print(f"Lowest score: {lowest_student} - {lowest_score}")

        # Exit
        elif choice == "7":
            print("Thank you for using the Student Score Tracker!")
            break

        else:
            print("Invalid choice. Please choose an option from 1 to 7.")


if __name__ == "__main__":
    main()