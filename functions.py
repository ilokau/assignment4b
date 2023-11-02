# File name: functions.py
# Author: Ilona Kauppila
# Description: Functions for the student list management program

import json

# definition for the Student class


class Student:
    def __init__(self, first_name, last_name, email, location_pref):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location_pref = location_pref

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nE-mail: {self.email}\nStudy preference: {self.location_pref}\n"


# List of students
students = [
    Student("Mikko", "Mallikas", "mikko.mallikas@sapo.com", "On-site"),
    Student("Milla", "Mallikas", "milla.mallikas@sapo.com", "Remote"),
    Student("John", "Doe", "johndoe@email.com", "Both"),
    Student("Jane", "Doe", "doejane@email.com", "Both"),
    Student("Olli", "Omena", "anemoomena@hedelma.com", "Remote"),
    Student("Anna", "Appelsiini", "anappel@hedelma.com", "Remote"),
    Student("Elli", "Erinomainen", "ellieri@sapo.com", "On-site"),
    Student("Hermanni", "Joki", "hj@sapo.com", "Both"),
    Student("Rosanna", "Lee", "leeros@email.com", "On-site"),
    Student("Alivia", "Cabrera", "calivia@email.com", "On-site"),
    Student("Chelsea", "Singleton", "chelsing@email.com", "Both"),
    Student("Barney", "Richmond", "richbarn@email.com", "On-site"),
    Student("Jaden", "Bender", "jaden.bender@email.com", "Remote"),
    Student("Molly", "Rhodes", "molly12@email.com", "Both"),
    Student("Jane", "Doe", "janedoe@email.com", "Remote"),
    Student("Marco", "Bond", "marco098@email.com", "Both"),
    Student("Emilia", "Vega", "emive@hedelma.com", "Both"),
    Student("Minna", "Erinomainen", "minnaeri@sapo.com", "On-site"),
    Student("Sadie", "McDonald", "mcsadie@sapo.com", "Remote"),
    Student("Tony", "Steele", "steeltony@email.com", "Remote"),
    Student("Ray", "Pendleton", "rayray@email.com", "On-site"),
    Student("Tim", "Fields", "fieldtims@email.com", "Both"),
    Student("Mikko", "Mallinen", "mikko.mallinen@sapo.com", "Remote"),
    Student("Einari", "Virtanen", "einari@sapo.com", "Both"),
    Student("Matti", "Matikainen", "mattis@email.com", "On-site"),
    Student("Anni", "Korhonen", "annik@email.com", "Both"),
    Student("Olli", "Omenainen", "omenainenolli@hedelma.com", "On-site"),
    Student("Kaede", "Smith", "kaede7@email.com", "Remote"),
    Student("Shinobu", "Jacobs", "sj@email.com", "On-site"),
    Student("Ville", "Virtanen", "virtanenvill@sapo.com", "On-site"),
    Student("Vilma", "Virtanen", "vilma123@email.com", "Remote"),
    Student("Onni", "Omena", "onni789@email.com", "Both"),
    Student("Anni", "Korhonen", "anni123@email.com", "On-site"),
]


# Function to save the list of students into a JSON file
def save_list_to_file():
    with open(
        "students.json",
        "w",
    ) as file:
        student_data = [student.__dict__ for student in students]
        json.dump(student_data, file)


# Function to load student data from a JSON file
def load_list_from_file():
    try:
        with open("students.json", "r") as file:
            student_data = json.load(file)
            students.clear()  # Clearing the existing list
            for data in student_data:
                student = Student(
                    data["first_name"],
                    data["last_name"],
                    data["email"],
                    data["location_pref"],
                )
                students.append(student)
    except FileNotFoundError:
        # Error for when the file does not exist
        pass


# Printing the whole list function
def print_list():
    if not students:
        print("The student list is empty.")
    for student in students:
        print(student)


# Search function
def search_list(search_term):
    found = False
    for student in students:
        if (
            search_term in student.first_name
            or search_term in student.last_name
            or search_term in student.email
            or search_term in student.location_pref
        ):
            print("Search results:")
            print(student)
            found = True
    if not found:
        print("Student(s) not found.")


# Add a new student function
def add_to_list(first_name, last_name, email, location_pref):
    new_student = Student(first_name, last_name, email, location_pref)
    students.append(new_student)
    save_list_to_file()


# Delete function which asks for first name, last name and e-mail for precision
def delete_from_list(first_name, last_name, email):
    to_delete = None
    for student in students:
        if (
            first_name == student.first_name
            and last_name == student.last_name
            and email == student.email
        ):
            to_delete = student
            break
    if to_delete is not None:
        students.remove(to_delete)
        save_list_to_file()
        print("Student removed successfully!")
    else:
        print("Student not found.")


# Sort function with a selection which field to sort by alphabetically
def sort_list(
    by_first_name=True,
    by_last_name=False,
    by_email=False,
    by_location_pref=False,
    reverse=False,
):
    if not (by_first_name or by_last_name or by_email or by_location_pref):
        print("Please select a valid sorting criteria.")
        return

    sorting_key = None
    if by_first_name:
        sorting_key = lambda student: student.first_name
    elif by_last_name:
        sorting_key = lambda student: student.last_name
    elif by_email:
        sorting_key = lambda student: student.email
    elif by_location_pref:
        sorting_key = lambda student: student.location_pref

    students.sort(key=sorting_key, reverse=reverse)
    save_list_to_file()


# Function that counts the number of students that chose each option for study preference
def count_study_pref(students):
    on_site_count = 0
    remote_count = 0
    both_count = 0
    total_students = len(students)

    for student in students:
        location_pref = student.location_pref.capitalize()
        if location_pref == "On-site":
            on_site_count += 1
        if location_pref == "Onsite":
            on_site_count += 1
        if location_pref == "Remote":
            remote_count += 1
        if location_pref == "Both":
            both_count += 1
    return total_students, on_site_count, remote_count, both_count
