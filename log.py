from colorama import Fore,init
init(autoreset=True)

def log(number,url):
       print(Fore.YELLOW + number + Fore.RED + " : " + Fore.GREEN + "Successfully" + Fore.RED + " -> " + Fore.LIGHTBLUE_EX + url)

log("11228","gay")