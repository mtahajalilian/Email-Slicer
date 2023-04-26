import re
import os
import colorama


def clear_screen():
    '''This function clear before printing the result of the slicing'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_screen()
colorama.init(autoreset=True)

email = input('Enter email here: ')
username = re.search(r'^[^@]+', email).group()
domain = re.search(r'[^@]+$', email).group()

print(colorama.Style.BRIGHT + colorama.Fore.BLUE + '\n\nUsername:', colorama.Style.BRIGHT + colorama.Fore.RED + username)
print(colorama.Style.BRIGHT + colorama.Fore.BLUE + 'Domain:', colorama.Style.BRIGHT + colorama.Fore.RED + domain, '\n\n')
