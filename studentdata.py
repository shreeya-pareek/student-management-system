import json

# Load existing data
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

# Save data function
def save_data():
 with open("students.json", "w") as file:
        json.dump(students, file)

# Add student
def add_student():
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    # Prevent duplicate roll number
    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists!\n")
            return

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_data()
    print("Student added successfully!\n")

# View students
def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
        print()

# Search student
def search_student():
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s["roll"] == roll:
            print(f"Found: Name: {s['name']}, Marks: {s['marks']}\n")
            return
    print("Student not found.\n")

# Delete student
def delete_student():
    roll = int(input("Enter roll number to delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data()
            print("Student deleted.\n")
            return
    print("Student not found.\n")

# Main menu loop
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")