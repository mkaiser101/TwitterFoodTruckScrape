import pickle
import base64
import sys
from getpass import getpass

def main():
    
    if sys.version_info < (3,0):
        username = str(raw_input("Username: "))
        password = getpass("Password: ")
        password = base64.b64encode(password)
    else:
        username = input("Username: ")
        password = getpass("Password: ")
        password = base64.b64encode(password.encode())
    with open("creds.bin", 'wb') as writefile:
        creds = (username,password)
        pickle.dump(creds, writefile)

if __name__ == '__main__':
    main()