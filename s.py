def calculate_average(scores):
    total = sum (scores)
    average =total/len(scores)
    return average

def search_student(students):
    name = input ("Enter student name;")

    for student in students:
        if student["name"].lower()== name.lower():
           print("student found!")
           print("Name:" , student ["name"])
        print("Scores:",  students ["scores"])
        print ("Averange:", student ["averange"])
        return
print("students not found.")

 


