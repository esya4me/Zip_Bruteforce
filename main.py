from zipfile import ZipFile
from os import system, path
from sys import argv, exit


def get_password_list(passwordlist):
    with open(passwordlist, "r") as file:
        return file.readlines()


def unzip(directory_to_unzip, file, password):
    myzip = ZipFile(file, "r")
    myzip.setpassword(password.encode('utf-8'))
    myzip.extractall(directory_to_unzip)
    myzip.close()


get_password_list("passwordlist.txt")


def main():
    global file, database, dirname
    passwords = get_password_list(database)
    for password in passwords:
        try:
            unzip(dirname, file, password)
            print("success:", password)
            exit()
        except RuntimeError:
            pass
            print("password not found")
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/