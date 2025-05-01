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


def add_task(file_name):
    while True:
        username = input("Please enter the username of the person to whom the "
                         "task will be assigned: ")
        if user_exists(username, "user.txt"):
            break
        else:
            print("User does not exist.")
            continue
    title = input("Please enter the title of the task: ")
    description = input("Please enter a description of the task: ")
    date_assigned = datetime.datetime.now().date()
    due_date = get_due_date(date_assigned)
    completed = get_completion_status()
    with open(file_name, "a") as file:
        file.write(
            f"\n{username}, {title}, {description}, "
            f"{date_assigned.strftime("%d")} "
            f"{date_assigned.strftime("%b")} "
            f"{date_assigned.strftime("%Y")}, "
            f"{due_date.strftime("%d")} "
            f"{due_date.strftime("%b")} "
            f"{due_date.strftime("%Y")}, "
            f"{completed}")


def get_due_date(date_assigned):
    while True:
        try:
            due_year = int(input(
                "Please enter the year that the task is due: "))
            if due_year <= 0:
                raise ValueError("Value must be positive.")
            due_month = int(input(
                "Please enter the month that the task is due: "))
            if due_month <= 0:
                raise ValueError("Value must be positive.")
            due_day = int(input(
                "Please enter the day of the month that the "
                "task is due: "))
            if due_day <= 0:
                raise ValueError("Value must be positive.")
            due_date = datetime.datetime(due_year, due_month, due_day).date()
            if due_date < date_assigned:
                raise Exception("Due date cannot be before the current date.")
        except ValueError as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            continue
        break
    return due_date


def get_completion_status():
    while True:
        completed = input("Has the task been completed yet? Y/N: ").upper()
        if completed == "Y":
            completed = "Yes"
            break
        elif completed == "N":
            completed = "No"
            break
        else:
            print("Response not recognised.")
    return completed


def view_tasks(file_name, user=None):
    with open(file_name, "r") as file:
        lines = file.readlines()
    for line in lines:
        task = line.split(", ")
        if user is None:
            print_task(task)
        elif user == task[0]:
            print_task(task)


def print_task(task):
    print("__________________________________________________________\n")
    print("{:20} {:20}".format(*["Task:", task[1]]))
    print("{:20} {:20}".format(*["Assigned to:", task[0]]))
    print("{:20} {:20}".format(*["Date assigned:", task[3]]))
    print("{:20} {:20}".format(*["Due date:", task[4]]))
    print("{:20} {:20}".format(*["Task complete?:", task[5].strip("\n")]))
    print("Task description:\n " + task[2])
    print("__________________________________________________________")


def display_statistics():
    with open("tasks.txt", "r") as file:
        task_lines = file.readlines()
    num_tasks = len(task_lines)
    with open("user.txt", "r") as file:
        user_lines = file.readlines()
    num_users = len(user_lines)
    print(f"There are a total of {num_tasks} tasks and {num_users} users.")


# ====Login Section====
# Allow the user to log in.
current_user = login("user.txt")

if current_user == "admin":
    while True:
        # Present the menu to the user and
        # insure that the user input is converted to lower case.
        menu = input("Select one of the following options:\n"
                     "r - register user\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "d - display statistics\n"
                     "e - exit\n").lower()

        if menu == 'r':
            register_user("user.txt")

        elif menu == 'a':
            add_task("tasks.txt")

        elif menu == 'va':
            view_tasks("tasks.txt")

        elif menu == 'vm':
            view_tasks("tasks.txt", current_user)

        elif menu == 'd':
            display_statistics()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")
else:
    while True:
        # Present the menu to the user and
        # insure that the user input is converted to lower case.
        menu = input("Select one of the following options:\n"
                     "a - add task\n"
                     "va - view all tasks\n"
                     "vm - view my tasks\n"
                     "e - exit\n").lower()

        if menu == 'a':
            add_task("tasks.txt")

        elif menu == 'va':
            view_tasks("tasks.txt")

        elif menu == 'vm':
            view_tasks("tasks.txt", current_user)

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")
