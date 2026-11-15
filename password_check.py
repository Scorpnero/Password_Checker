import os
from password_checker import check_passwoed
from create_pass import create_password
import sys

os.system('cls' if os.name == 'nt' else 'clear')
print("""
▄▖              ▌    ▌     ▌     
▙▌▀▌▛▘▛▘▌▌▌▛▌▛▘▛▌  ▛▘▛▌█▌▛▘▙▘█▌▛▘
▌ █▌▄▌▄▌▚▚▘▙▌▌ ▙▌▄▖▙▖▌▌▙▖▙▖▛▖▙▖▌ 
                                  """)
def start1():
    input1 = input('''┌──(root㉿ScorpNero)-[~/tools]
    └─$
    [1]check Password
    [2]create Password
    [3]Exit

    Please Enter number:''')

    if input1 == "1":
        password=input("Enter Password: ")
        check_passwoed(password)
    elif input1 =="3":
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
    elif input1 =='2':
        create_password()
start1()

