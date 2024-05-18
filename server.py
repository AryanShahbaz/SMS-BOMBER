from colorama import Fore,init
init(autoreset=True)

def select_server() :
       server_num =input(Fore.LIGHTGREEN_EX+"Please select server\nServer 1 or Server 2\n"+Fore.GREEN +"-> ")
       # print(Fore.YELLOW + "DEBUG: You entered: " + server_num)
       if server_num == '1':
              return(1)
       elif server_num == '2':
              return(2)
       else:
              return(Fore.RED + "WRONG INPUT")