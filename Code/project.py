import student
import classes
import validate_user
import csv
import sys
import os


def login():
    username = input("Enter username (admin): ").strip()
    password = input("Enter password (admin): ").strip()

    try:
        with open("password_hashes.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                if row["username"] == username and row["hashed_password"] == validate_user.hash_password(password):
                    print(welcome(username))
                    return True
            # If loop does not return true it means user is not registered
            sys.exit("Authentication Failed")
    except FileNotFoundError:
        sys.exit("File not found.")

def welcome(name):
    return (f"\nWelcome {name}! to attendance dashboard.\n")


def menu():
    print("Select an operation:\n```````````````````\n1- Mark Attendance\n2- View Attendance\n3- Add New Student\n4- Exit")
    choice = int(input("Enter here: "))
    return choice


def mark_attendance():
    print("\nCreate a new class")
    print("``````````````````")
    clas = classes.Classes.get()
    print("\nMark the attendance")
    print("```````````````````")
    print("ID\tName\t\tAttendance")
    # Check file exists
    file_exists = os.path.exists("attendance_detail.csv")

    with open("student_detail.csv", "r") as reader:
        with open("attendance_detail.csv", "a") as file:
            field_names = ["date", "subject", "id", "name", "attendance"]
            writer = csv.DictWriter(file, fieldnames = field_names)

            # Write the header only if the file doesn't exist
            if not file_exists:
                writer.writeheader()

            std_file = csv.DictReader(reader)
            for row in std_file:
                print(f"{row['id']}\t{row['name']}\t: ", end = "")
                attend = input().strip().upper()
                if attend in ["A", "P", "L"]:
                    writer.writerow({'id': row['id'], 'name': row['name'], 'subject': clas.subject, 'date': clas.date, 'attendance' : attend})
                else:
                    writer.writerow({'id': row['id'], 'name': row['name'], 'subject': clas.subject, 'date': clas.date, 'attendance' : 'U'})

def add_new_student():
    print("\nAdd a new student")
    print("`````````````````")
    std = student.Student.get()

    # Check file exists
    file_exists = os.path.exists("student_detail.csv")
    with open("student_detail.csv", "a") as file:
        field_names = ["id","name"]
        csv_file = csv.DictWriter(file, fieldnames = field_names)

        # Write the header only if the file doesn't exist
        if not file_exists:
            csv_file.writeheader()
        csv_file.writerow({"id": std.id, "name" : std.name})

def view_attendance():
    print()
    clas = classes.Classes.get()
    print(f"\nAttendance List for {clas.subject} on {clas.date}")
    print("````````````````````````````````````````````")
    print("ID\tName\t\tAttendance")
    try:
        with open("attendance_detail.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['subject'] == clas.subject and row['date'] == str(clas.date):
                    print(f"{row['id']}\t{row['name']}\t: {row['attendance']}")
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if login():
        while True:
            input()
            os.system('clear')
            choice = menu()

            if choice == 1:
                mark_attendance()
            elif choice == 2:
                view_attendance()
            elif choice == 3:
                add_new_student()
            elif choice == 4:
                print("\n\nThanks for using the attendance system 😊.")
                break
            else:
                sys.exit("Invalid selection.")


if __name__=="__main__":
    main()





