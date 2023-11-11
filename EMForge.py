
import time 

print('''

 /$$$$$$$$ /$$      /$$ /$$$$$$$$                                     
| $$_____/| $$$    /$$$| $$_____/                                     
| $$      | $$$$  /$$$$| $$     /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$   | $$ $$/$$ $$| $$$$$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__/   | $$  $$$| $$| $$__/| $$  \ $$| $$  \__/| $$  \ $$| $$$$$$$$
| $$      | $$\  $ | $$| $$   | $$  | $$| $$      | $$  | $$| $$_____/
| $$$$$$$$| $$ \/  | $$| $$   |  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$
|________/|__/     |__/|__/    \______/ |__/       \____  $$ \_______/
                                                   /$$  \ $$          
                                                  |  $$$$$$/          
                                                   \______/           

''')

time.sleep(2)
print("Developed by Harry Priestley")
time.sleep(2)
print("Any information can be seen in my Git repo")
time.sleep(2)
print("BigSimp06/EMForge")
print('''                                                 ''')
time.sleep(2)
print("-------------------------------------------------------")


def seperation(wordlist_Path, domain):
    file = open(wordlist_Path, 'r')
    names = file.readlines()
    for name in names:
        name_Parts = name.strip().split(' ')
        if len(name_Parts) == 2:
            firstname, lastname = name_Parts
            firstname = str(firstname)
            lastname = str(lastname)
            print(f"{firstname}{lastname}@{domain}")
            print(f"{lastname}{firstname}@{domain}")
            print(f"{firstname}@{domain}")
            print(f"{lastname}@{domain}")
            print(f"{lastname}.{firstname[0]}@{domain}")
            print(f"{firstname}.{lastname[0]}@{domain}")
            print('''                                                 ''')
            time.sleep(2)
        else:
            firstname = name_Parts[0]
            firstname = str(firstname)
            lastname = None
            print(f"{firstname}@{domain}")
            print('''                                                  ''')



domain = input("Email Domain: ")
wordlist_Path = input("wordlist path: ")
print('''                                                 ''')
print("-------------------------------------------------------")

try:
    seperation(wordlist_Path, domain)
except FileNotFoundError:
    print(f"Error file not found")
except Exception as e:
    print(f"an unknown error has occured {e}")
finally:
    time.sleep(2)
    print('''
⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣴⡏⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣄⠀⠀⠀⠀⢀⣼⣿⣁⣤⡶⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⡄⠀⢠⣷⣾⣿⣿⣿⣿⣁⣀⡀⠀⠀
⠀⠀⠀⢀⣠⣴⣾⡿⠟⠋⠉⠀⠈⢿⣿⣿⠷⠀⣾⠿⠛⣿⣿⠿⠛⠋⠁⠀⠀⠀
⠀⢲⣿⡿⠟⠋⠁⠀⠀⠀⠀⢀⣀⣈⣁⣀⣀⣀⣀⣀⣀⣁⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠈⠁⠀⠀⠀⢠⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⢛⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀''')
    print("Thank you for using my tool!")
