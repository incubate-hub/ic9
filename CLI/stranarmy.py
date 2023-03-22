import time
import sys
import os


def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting : ")
time.sleep(5)
os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
slowprint("    \033[91mOnionSearch")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
 
  ____           _ _                __  __
|  _ \ __ _  __| (_)_   _ _ __ ___ \ \/ /
| |_) / _` |/ _` | | | | | '_ ` _ \ \  / 
|  _ < (_| | (_| | | |_| | | | | | |/  \ 
|_| \_\__,_|\__,_|_|\__,_|_| |_| |_/_/\_\
                                         

 \033[97m             
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mBy :RadiumX\033[97m")
print(" ")
print("1-Enter the url that you wanna scan:")
print("")

print("2-Exit")
print(" ")
print("")
x=input("\033[92m[?] \033[96mEnter any option ==>")
if x==('1') :
               slowprint("")
               os.system('python3 vtcli.py -u https://www.facebook.com/')
               
if x==('2') :
               slowprint("")
               os.system('exit')
               os.system('mpg123 lion.mp3 >/dev/null 2>&1')

  
slowprint("")
slowprint("")


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)


