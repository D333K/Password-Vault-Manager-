# import random
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

# ========================

def search_website(website_data): 

    id_website = int(input("Enter The Website ID: "))
    found = False

    for website in website_data:

        if website["ID"] == id_website:
            for website_key, website_value in website.items():
                print(f"- {website_key} : {website_value}")

            print('-' * 22)

            found = True

    if not found:
        print("Sorry, ID not found.")

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

# ========================

def generate_password(website_data, id):

    letters_for_password = string.ascii_letters + string.digits + "!@#$%^&*_-~" 
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

    next_id += 1

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
    
    # else:
    #     print("Enter Number Not Negative Numbers Or Text!!!")
    #     input("Press To Continue...")



    # "ABCDEFGHIKJLMNOPQRSTUVWXYZabcdefghikjlmnopqrstuvwxyz1234567890!@#$%^&*_-~"
    # password = input("Enter The Password: ")

    # password_length = input("Enter The Length Of Password: ")

    # Here a problem!
    # The this function make password more than wht user want!
    # Fix it!
    # print(i)
    # password += random.choice(letters_for_password)

# I Still Don't Find Solution For This Problem:(.
# if next_id >= 1:
#     next_id = next_id + 1

# else:
#     next_id = 1 # And Here It's The Same Problem:/.

# Here Problem But I Don't What Is It:/.
# global next_id # Here Problem But I Don't What Is It:/.
# The Problem It's In The Zero Value:|.
# No, The Solution Is Not In Change The Zero Value


# Exception has occurred: UnboundLocalError
# cannot access local variable 'next_id' where it is not associated with a value
#   File "/media/dark-knight/وحدة تخزين جديدة/Engineer_Thinking_Challenges/Password-Vault-Manager/main.py", line 12, in add_password
#     next_id = next_id + 1
#               ^^^^^^^
#   File "/media/dark-knight/وحدة تخزين جديدة/Engineer_Thinking_Challenges/Password-Vault-Manager/main.py", line 71, in <module>
#     add_password()
#     ~~~~~~~~~~~~^^
# UnboundLocalError: cannot access local variable 'next_id' where it is not associated with a value


