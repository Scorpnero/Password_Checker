import string
from colorama import Fore,Style
from pathlib import Path




file_path = Path(__file__).parent / "passwords.txt"
with open(file_path, "r", encoding="utf-8") as file:
    common_password = set(file.read().splitlines())


def check_passwoed(password):
    score = 0 
    suggestions = []
    
    if len(password)>=12:
        score+=2
    elif len(password)>=8:
        score+=1
    else:
        suggestions.append(Fore.LIGHTRED_EX+'  -The password must be at least 8 characters long! ')
    if any(c.islower()for c in password):
     
        score+=1
    else:
        
        suggestions.append(Fore.YELLOW+'  -The password must contain a lowercase letter.')
    if any(c.isupper()for c in password):
        
        score+=1
    else:
        
        suggestions.append(Fore.YELLOW+'  -The password must contain an uppercase letter.')
    if any(c.isdigit()for c in password):
        
        score+=1
    else:
        
        suggestions.append(Fore.YELLOW+   '-The password must contain a number.')
    if any(c in string.punctuation for c in password):
       
        score+=1
    else:
     
        suggestions.append(Fore.YELLOW+'  -The password must contain a special character[@-!-#-$-%-?]')
    if password.lower() in common_password:
        score = 0
        print(Fore.LIGHTRED_EX+'Your password is very low!')
    else:
        for i in suggestions:
            print(i)
        print("---------------------")
        if score<=3:
            print(Fore.LIGHTRED_EX+'[+]'+Fore.LIGHTYELLOW_EX+'Your Password is Low!')
            blocks = 1
            color = Fore.LIGHTRED_EX
            status =Fore.LIGHTRED_EX+'Low'
        elif score<=5:
            print(Fore.BLUE+'[+]'+Fore.LIGHTBLUE_EX+'Your password is Normal.')
            blocks = 2
            color = Fore.LIGHTYELLOW_EX
            status=Fore.LIGHTWHITE_EX+'Normal'
        else:
            print(Fore.GREEN+'[+]'+Fore.LIGHTWHITE_EX+'Your password is Good.')
            blocks = 3
            color = Fore.LIGHTGREEN_EX
            status=Fore.LIGHTGREEN_EX+'Good'
        bar = color + "█" * (blocks * 5) + Style.RESET_ALL
        empty = Fore.WHITE + "░" * ((3 - blocks) * 5)
        print(f"{bar}{empty}{Style.RESET_ALL} {status}")





    


