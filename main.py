from random import randint
import string
import os
import termcolor
import pyfiglet

website_info = [] # Save The Password And Website And UserName Information Of User.

next_id  = 0

def print_message(message):
    '''This Method Print The Message After Operation Successfully Done.'''
    print('-' * 22)
    print(f"{message} Successfully!")
    input("Press To Continue...")

# ========================

def add_password(website_data, id):

    website_name = input("Enter The Website: ").lower().strip()
    password = input("Enter The Password: ").strip()
    username = input("Enter The UserName: ").strip()

    website = {
        "ID" : id,
        "Website" : website_name,
        "Password" : password,
        "UserName" : username,
    }
    website_data.append(website)

    print('-' * 22)

    for website_key, website_value in website.items():
        print(f"- {website_key} : {website_value}")

    print_message("Added")

# ========================

def view_info(website_data):

    for website in website_data:
        for website_key, website_value in website.items():
            print(f"- {website_key} : {website_value}")

        print('-' * 22)

    input("Press To Continue...")

# ========================

def search_website(website_data): 

    id_website = int(input("Enter The Website ID: "))
    found = False

    for website in website_data:

        if website["ID"] == id_website:
            print('-' * 22)
            for website_key, website_value in website.items():
                print(f"- {website_key} : {website_value}")

            print('-' * 22)

            found = True

    if not found:
        print("Sorry, ID not found.")

    input("Press To Continue...")

# ========================

def delete_website(website_data): 

    website_id = int(input("Enter The Website ID: "))
    found = False

    for website in website_data:

        if website["ID"] == website_id:
            for website_kye, website_value in website.items():
                print(f"- {website_kye} : {website_value}")

            website_data.remove(website)

            print_message("Deleted")
            print('-' * 22)

            found = True
            break

    if not found:
        print("Sorry, ID not found.")
        input("Press To Continue...")

# ========================

def generate_password(website_data, id):

    letters_for_password = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "1234567890!"
        "@#$%^&*_-~"
        )
    password = ""

    website_name = input("Enter The Website: ").lower().strip()
    username = input("Enter The UserName: ").strip()
    password_length = int(input("Enter The Length Of Password: "))

    for i in range(password_length):
        index = randint(0, len(letters_for_password) - 1)
        password += letters_for_password[index]

    website = {
        "ID" : id,
        "Website" : website_name,
        "Password" : password,
        "UserName" : username,
    }
    website_data.append(website)

    print('-' * 22)
    for website_key, website_value in website.items():
            print(f"- {website_key} : {website_value}")

    print_message("Generated")

# ========================

def clear_lines(report_operation):

    '''This Method Clear Depending On The OS You Use It And Make Title Of The Operation The Have User Chosen It.'''
    os.system("cls" if os.name == "nt" else "clear")
    
    print('=' * 12, end=' ')
    print(report_operation, end=' ')
    print('=' * 12, end="\n\n")

# ========================

while True:

    clear_lines("Password Vault")

    print(" 1.Add Password")
    print(" 2.View Password")
    print(" 3.Search Website")
    print(" 4.Delete Website")
    print(" 5.Generate Password")
    print(" 0.Exit")
    
    print("_" * 12)
    UserSelection = int(input("Choose An Operation: "))

    try:
        if UserSelection < 0:
            raise ValueError()
        elif UserSelection == 1:
            clear_lines("Add Password")
            next_id += 1
            add_password(website_info, next_id)

        elif UserSelection == 2:
            clear_lines("View All Password")
            view_info(website_info)

        elif UserSelection == 3:
            clear_lines("Search Website")
            search_website(website_info)

# Here a problem.
# ex: if the user adds 2 websites and slected the delete option,
# and when user select add or generate option,
# the next_id will be 2 and this ID already exists and this a problem!

        elif UserSelection == 4:
            clear_lines("Delete Website")
            delete_website(website_info)
            next_id -= 1

        elif UserSelection == 5:
            clear_lines("Generate Password")
            next_id += 1
            generate_password(website_info, next_id)

        elif UserSelection == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print(termcolor.colored(pyfiglet.figlet_format("Created By Dark Knight"), color="black"))
            break

    except ValueError:
        print("Error in input! \nPlease enter a valid number.")
        input("Press To Continue...")