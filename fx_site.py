import requests
from bs4 import BeautifulSoup
import os
os.system('clear')

# Color --------
B="\033[0;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # Whit
# End Color -------

print(R+f'''
   (            )              )\ )                 )  
   )\  (     ( /(    (   (    (()/(      )  (    ( /(  
 (((_) )\ )  )\())  ))\  )(    /(_))  ( /(  )(   )\()) 
 )\___(()/( ((_)\  /((_)(()\  (_))_   )(_))(()\ ((_)\  
((/ __|)(_))| |(_)(_))   ((_)  |   \ ((_)_  ((_)| |(_) 
 | (__| || || '_ \/ -_) | '_|  | |) |/ _` || '_|| / /  
  \___|\_, ||_.__/\___| |_|    |___/ \__,_||_|  |_\_\  
       |__/    
       
{W}Telegram{R}
{W}Personal Account : {R}@L_N_X_0    
{W}Channels         : {R}@FLXIU - @cy_code

{G}Team :{G}
-> {W}@L_N_X_0 {G}(Mr.Dark)
-> {W}@Timoxr {G}(Rafik)
-> {W}@HUSS1N0 {G}(Hosin)

        {W}Code By Mr.Dark
        
        
''')

url = input("Please Enter Target \"URL\" :")

os.system('clear')

req = requests.get(url)

print(Y+f'''
Please Choose what do you need ?
00 - Exit

1 - images
2 - iframe
3 - class {R}(Not Available){Y}
4 - javaScript Files
5 - HyperLinks (<a>)
6 - Css Files
7 - Download Source Code From This Page

99 - Custom
''')

choose = int(input(W+"Select Number :"))

if choose == 00:
	print(R+"\noh <oo> bye bye")
	exit()
elif choose == 1:
	findtag = "img"
	getfrom = "src"
elif choose == 2:
	findtag = "iframe"
	getfrom = "src"
elif choose == 3:
	findtag = "*"
	getfrom = "class"
elif choose == 4:
	findtag = 'script'
	getfrom = "src"
elif choose == 5:
	findtag = "a"
	getfrom = "href"
elif choose == 6:
	findtag = "link"
	getfrom = "href"
elif choose == 7:
	html_output_name = input('Name for html file: ')
	req = requests.get(url, 'html.parser')

	with open(html_output_name, 'w') as f:
	    f.write(req.text)
	    f.close()
	print(G+"\n Success Saved File")   
elif choose == 99:
	get_findtag = input(W+"\nEnter Tags Name Example(a,img,script,iframe): ")
	get_from = input(W+"Get Data From Example(class,href,src): ")
	findtag = get_findtag
	getfrom = get_from
	
else:
	print(R+"\nError This Number Not Available Please Try Again")
	exit()
	
if choose != 7:
	bs = BeautifulSoup(req.text, "html.parser")

	if choose == 4 or choose == 5:
		for link in bs.findAll(findtag):
			print(f"{G}")
			print(link.get(getfrom))

	else:
		for link in bs.findAll(findtag):
			print(f"\n{Y}[+] {G}"+link.get(getfrom))

