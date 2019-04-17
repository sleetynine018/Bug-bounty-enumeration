#!/usr/bin/python

import time
import sys
import socket
from subprocess import call

cool_effect = "#"*60

print(cool_effect)
print("\n\tBug bounty enumeration\n\n")
print(cool_effect)
print("Use this script with the following target: https://wwww.example.com")
print("WARNING: Don't use this in any domain with a selected directory, like domain.com/en")


if (len(sys.argv) < 2):
	print("Please provide a domain/subdomain!")
	sys.exit(0)

if (len(sys.argv[1]) > 100):
	print("Are you sure that's a domain?!")
	sys.exit(0)

if "www" not in sys.argv[1]:
	print("Please provide 'www' in your url")
	sys.exit(0)

if "http" not in sys.argv[1]:
	print("Please provide 'http/https' ")






def nmap_scan(target):

	#Cant use http/https in nmap
	if "http" in target:
		type_of_connection, actual_target = target.split("//")
	else:
		actual_target = target

	#scan using the ip
	target = socket.gethostbyname(actual_target)

	
	print("\n\n"+cool_effect)
	print("\tNmap scan")
	print(cool_effect)

	print("Starting nmap scan on " + target + "\n\n")

	call('nmap -T4 -A -v -sV ' + target, shell=True)

	time.sleep(5)
	dir_scan(target)



def dir_scan(target):
	#TODO: Make dir scanner

	print("\n\n"+cool_effect)
	print("\tGetting robots.txt if it exists...")
	print(cool_effect)


	call("curl " + target + "/robots.txt", shell=True)


	time.sleep(5)

	security_headers_scan(target)



def security_headers_scan(target):

	shcheck_path = "~/Desktop/SecTools/shcheck.py"
	print("\n\n"+cool_effect)
	print("\tSecurity headers")
	print(cool_effect)


	call("python " + shcheck_path + " " + target + " -i -x", shell=True)


	time.sleep(5)

	waf_scan(target)



def waf_scan(target):

	#TODO:BETTER USE WITH HTTPS AND WWW
	print("\n\n"+cool_effect)
	print("\tWaf check")
	print(cool_effect)

	call("wafw00f " + target, shell=True)

	print("Good luck\nHappy hacking :)")





nmap_scan(sys.argv[1])