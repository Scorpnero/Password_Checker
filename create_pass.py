
import string
import secrets



def create_password():


    level = input(
        "Choose complexity [Easy/Normal/Hard]: "
    ).lower().strip()

    if level == 'easy':
        chars = string.ascii_letters
        length = 8

    elif level == 'normal':
        chars = string.ascii_letters + string.digits
        length = 12

    elif level == 'hard':
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 16

    else:
        print("Invalid difficulty!")
        return

    password = ''.join(
        secrets.choice(chars) for _ in range(length)
    )

    print("Your generated password:", password)
  

    




