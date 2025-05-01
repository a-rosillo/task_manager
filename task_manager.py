# =====importing libraries===========
import datetime
# ====Functions====


def read_users(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    # Put usernames and passwords into a list of dictionaries.
    users_out = []
    for line in lines:
        usr = line.split(', ')[0].strip("\n")
        pwd = line.split(', ')[1].strip("\n")
        users_out.append({"username": usr,
                          "password": pwd})
    return users_out


def login(file_name):
    # Read usernames and passwords
    users = read_users(file_name)
    print("Welcome\nPlease sign in")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if {"username": username, "password": password} in users:
            break
        elif user_exists(username, file_name):
            print("Password incorrect.\nPlease try again.")
        else:
            print("Username not found.\nPlease try again.")
    return username

    def register_user(file_name):
    print("Please enter the username and password")
    while True:
        username = input("Username: ")
        # Check whether username is already taken.
        if user_exists(username, file_name):
            print("An account already exists with this username\n"
                  "Please choose another username.")
            continue
        else:
            break
    while True:
        password_1 = input("Password: ")
        password_2 = input("Confirm password: ")
        if password_1 == password_2:
            break
        else:
            print("Passwords do not match. \nPlease try again.")
    with open(file_name, "a") as file:
        file.write(f"\n{username}, {password_1}")
    print("Password saved.")


def user_exists(user_to_check, file_name):
    existing_users = read_users(file_name)
    user_found = False
    for user in existing_users:
        if user_to_check == user["username"]:
            user_found = True
            break
    return user_found


# ====Login Section====
# Allow the user to log in.
current_user = login("user.txt")

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        register_user("user.txt")

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")