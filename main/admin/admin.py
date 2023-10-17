from time import sleep
import webbrowser as wb
from os import path, system


def clear():
    system('clear')


def menu():
    absolutePath = path.dirname(__file__)
    relPath = "../main/"
    fullPath = path.join(absolutePath, relPath)

    with open(fullPath + "start.py") as f:
        exec(f.read())
    quit()


logRelPath = "../../logs/"

f = open("main/admin/adminPassword.txt", "r")
password = f.read()
f.close

clear()

passwordCheck = input("Enter Password (Default is 0000): ")

if passwordCheck == password:
    print("Succsessfull Authorisation")
    sleep(1.5)

    clear()
    print("TOOLS")
    print("1: Set Admin Password")
    print("2: Open Files (Requires internet connection)")
    print("3: Open Log File (Requires internet connection)")
    print("Back to Main Menu (any key)")
    toolSel = input("Select the tool you want to use: ")

    if toolSel == "1":  # Admin Password Changer Tool
        f = open("main/admin/adminPassword.txt", "r")
        password = f.read()
        f.close
        clear()
        print("Current Password is " + password)
        passwordTemp = input("Enter New password: ")
        confirm = input("Enter Old Password: ")

        if confirm != password:
            print("Hm. The old password you entered is wrong.")
            print("Returning to Main Menu...")
            sleep(1.5)
            menu()

        if password == passwordTemp:
            print("New password can not be the same as old password.")
            print("Returning to Main Menu...")
            sleep(1.5)
            menu()

        if confirm == password:
            with open(path.dirname(__file__) + '/../main/admin/adminPassword.txt', 'w') as f:
                f.write(str(passwordTemp))
                f.flush
                f.buffer

            print("Successfully changed password to " + passwordTemp)
            print("Returning to Main Menu...")
            sleep(1.5)
            menu()

    elif toolSel == "2":  # Web-based file explorer
        wb.open(path.dirname(__file__) + "../../")
        menu()
    elif toolSel == "3":
        wb.open(path.dirname(__file__) + "../../logs/game.log")
        menu()
    else:
        menu()
else:
    print("Invalid password. Returning to Main Menu...")
    sleep(1.5)
    menu()
