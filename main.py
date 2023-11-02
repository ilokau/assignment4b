# File name: main.py
# Author: Ilona Kauppila
# Description: The main code for the student list management program

from functions import (  # Importing functions from the functions file
    Student,
    students,
    save_list_to_file,
    load_list_from_file,
    print_list,
    search_list,
    add_to_list,
    delete_from_list,
    sort_list,
    count_study_pref,
)

load_list_from_file()  # Load the list of students from a file

while True:
    print("\nWelcome to the student management system!")
    print("1. Display the list of students.")
    print("2. Search for a student.")
    print("3. Add a new student.")
    print("4. Remove a student from the list.")
    print("5. Sort and see the sorted list.")
    print("6. Display study location preference statistics.")
    print("7. Exit the program.")
    choice = input("Enter your choice:")

    if choice == "1":
        while True:
            print_list()  # Calling the print_list function to print the complete list of students
            print("1. Display the list again")
            print("2. Return to start.")
            print("3. Exit program.")
            print_choice = input("Enter your choice.")
            if print_choice == "1":
                continue
            if print_choice == "2":
                break
            if print_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print("Please enter a valid choice.")

    elif choice == "2":
        while True:
            search_term = input(
                "Enter your search term. You can search students by first name, last name, study preference or e-mail."
            )
            search_list(
                search_term
            )  # Calling the search_list function with the search term variable
            print("1. Search again.")
            print("2. Return to start.")
            print("3. Exit program.")
            search_choice = input("Enter your choice.")
            if search_choice == "1":
                continue
            if search_choice == "2":
                break
            if search_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print(
                    "Please enter a valid choice (1 to search again, 2 to return to start, 3 to exit program)."
                )

    elif choice == "3":
        while True:
            print("Adding a new student.")
            first_name = ""
            last_name = ""
            email = ""
            location_pref = ""

            while not first_name:
                first_name = input("Please enter first name.").capitalize()
                if not first_name:
                    print("First name cannot be empty. Please try again.")

            while not last_name:
                last_name = input("Please enter last name.").capitalize()
                if not last_name:
                    print("Last name cannot be empty. Please try again.")

            while not email:
                email = input("Please enter e-mail address.")
                if not email:
                    print("E-mail cannot be empty. Please try again.")
            while True:
                location_pref = input(
                    "Please enter preferred studying location (On-site, remote or both)."
                ).capitalize()
                if location_pref in ["On-site", "Onsite", "Remote", "Both"]:
                    break

                print("Please enter a valid choice (On-site, remote, or both).")
                invalid_choice = input(
                    "Enter '1' to try again, '2' to return to the start, or '3' to exit: "
                )
                if invalid_choice == "1":
                    continue
                elif invalid_choice == "2":
                    break
                elif invalid_choice == "3":
                    print("Exiting program. Bye!")
                    exit()
                else:
                    print("Invalid choice. Please enter '1', '2', or '3'.")

            add_to_list(
                first_name, last_name, email, location_pref
            )  # Calling the add_to_list function
            print("Student added successfully!")
            print("1. Add another student.")
            print("2. Return to start.")
            print("3. Exit program.")
            add_choice = input("Enter your choice.")
            if add_choice == "1":
                continue
            if add_choice == "2":
                break
            if add_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print("Please enter a valid choice.")

    elif choice == "4":
        while True:
            print("Removing a student.")
            first_name = input("Please enter first name.").capitalize()
            last_name = input("Please enter last name.").capitalize()
            email = input("Please enter e-mail address.")
            delete_from_list(
                first_name, last_name, email
            )  # Calling the delete_from_list function
            print("1. Remove another student.")
            print("2. Return to start.")
            print("3. Exit program.")
            add_choice = input("Enter your choice.")
            if add_choice == "1":
                continue
            if add_choice == "2":
                break
            if add_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print("Please enter a valid choice.")

    elif choice == "5":
        while True:
            print("Sorting the list alphabetically based on sort criteria:")
            print("1. Sort by first name")
            print("2. Sort by last name.")
            print("3. Sort by e-mail address.")
            print("4. Sort by study location preference.")
            sorting_criteria = input("Please enter sorting criteria.")
            if sorting_criteria == "1":
                sort_list(
                    by_first_name=True,
                    by_last_name=False,
                    by_email=False,
                    by_location_pref=False,
                    reverse=False,
                )  # Call the sort_list function with specified sorting criteria (first name)
            elif sorting_criteria == "2":
                sort_list(
                    by_first_name=False,
                    by_last_name=True,
                    by_email=False,
                    by_location_pref=False,
                    reverse=False,
                )  # Call the sort_list function with specified sorting criteria (last name)
            elif sorting_criteria == "3":
                sort_list(
                    by_first_name=False,
                    by_last_name=False,
                    by_email=True,
                    by_location_pref=False,
                    reverse=False,
                )  # Call the sort_list function with specified sorting criteria (e-mail)
            elif sorting_criteria == "4":
                sort_list(
                    by_first_name=False,
                    by_last_name=False,
                    by_email=False,
                    by_location_pref=True,
                    reverse=False,
                )  # Call the sort_list function with specified sorting criteria (location preference)
            else:
                print("Please enter a valid choice.")
            print("List sorted successfully.")
            print_list()
            print("1. Sort list again.")
            print("2. Return to start.")
            print("3. Exit program.")
            sort_choice = input("Enter your choice.")
            if sort_choice == "1":
                continue
            if sort_choice == "2":
                break
            if sort_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print("Please enter a valid choice.")

    elif choice == "6":
        while True:
            total_students, on_site_count, remote_count, both_count = count_study_pref(
                students
            )  # Call the count_study_pref function with the 'students' list
            print(f"Total Students on list: {total_students}")
            print(f"Prefer on-site: {on_site_count} students")
            print(f"Prefer remote: {remote_count} students")
            print(f"Prefer both: {both_count} students")
            print("1. Display statistics again.")
            print("2. Return to start.")
            print("3. Exit program.")
            stats_choice = input("Enter your choice.")
            if stats_choice == "1":
                continue
            if stats_choice == "2":
                break
            if stats_choice == "3":
                print("Exiting program. Bye!")
                exit()
            else:
                print("Please enter a valid choice.")
