from colorama import Fore,init 
import requests
import socket 
init()




hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
http = requests.get("https://api.ipify.org/").text

print(Fore.GREEN+"[+] "+Fore.LIGHTCYAN_EX+"Your Local IP : "+Fore.WHITE+ip_local)
print(Fore.GREEN+"[+] "+Fore.LIGHTCYAN_EX+"Your Public IP : "+Fore.WHITE+http)