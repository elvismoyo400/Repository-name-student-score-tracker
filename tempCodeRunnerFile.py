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

    
        if choice == "1":
            name = input("Enter student name: ").strip()

            try:
                score = float(input("Enter student score: "))
                students[name] = score
                print(f"Added {name} with score {score}.")
            except ValueError:
                print("Invalid score. Please enter a number.")

        
        elif choice == "2":
            if not students:
                print("No students recorded yet.")
            else:
                print("\nList of Students:")
                for name, score in students.items():
                    print(f"- {name}: {score}")

        
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("This feature is not available yet.")


if __name__ == "__main__":
    main()