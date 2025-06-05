#the aim is to organize and store passwords in a file but the passwords will be encrypted, however ther eiwll be a master password that will be used to decrypt any of these paswwords where necessary
from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password: ")
key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

def view():
    with open('passwords.pdf', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "|  Password:", fer.decrypt(passw.encode()).decocde())


def add():
    #get user name and password then store it in a file
    name = input("Username: ")
    pwd = input("Password: ")

    with open('passwords.pdf', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view exiting one (view/add), press q to quit: ").lower()
    if mode == "q":
        quit() 
    elif mode == "view":
        view() 
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue 