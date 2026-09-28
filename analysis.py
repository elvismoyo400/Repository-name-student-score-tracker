def get_highest_score(students):
    if not students:
        print("No students available")
        return

    highest = students[0]

    for student in students:
        if student["score"] > highest["score"]:
            highest = student

    print(f"Highest Score: {highest['name']} - {highest['score']}")


def get_lowest_score(students):
    if not students:
        print("No students available")
        return

    lowest = students[0]

    for student in students:
        if student["score"] < lowest["score"]:
            lowest = student

    print(f"Lowest Score: {lowest['name']} - {lowest['score']}")


get_highest_score(students)
get_lowest_score(students)