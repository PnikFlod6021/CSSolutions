import re
def validate_password(password):
    uppercase = len(re.findall('[A-Z]', password)) > 1
    lowercase = len(re.findall('[a-z]', password)) > 1
    number = len(re.findall('[0-9]', password)) > 0
    char = len(re.findall('[@$!#%*?&]', password)) > 0
    length = len(password) > 7
    return uppercase and lowercase and number and char and length

def main():
    while True:
        password = input("Enter a password")
        if validate_password(password):
            print("password accepted")
            break
        elif password in open('common_passwords.txt', 'r').read():
            print("password too common")
            break
        else:
            print("Invalid password")
            break
main()
while True:
    response = input("Enter a new password (Y/N)").lower()
    if response == "y":
        main()
    elif response == "n":
        break
    else:
        print("Invalid Input")


