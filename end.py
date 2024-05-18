import pyfiglet
from colorama import Fore,init
init(autoreset=True)

def bye_text():
       fig=pyfiglet.Figlet(font='slant')
       ascii_art = fig.renderText("Good Bye")
       print(Fore.LIGHTYELLOW_EX + ascii_art)