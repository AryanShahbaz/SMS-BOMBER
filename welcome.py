import pyfiglet
from colorama import Fore,init
init(autoreset=True)

def welcome_text() :
       text=pyfiglet.figlet_format("SmS BoooMBER",font="slant")
       print(Fore.RED + text)
       print(Fore.BLUE + "\t\t\t\tBy:Aryan")