#!/usr/bin/python

import time
import sys
import socket
from subprocess import call

cool_effect = "#"*60

print(cool_effect)
print("\n\tBug bounty enumeration\n\n")
print(cool_effect)
ṕrint("WARNING: Don't use this in any domain with a selected directory, like domain.com/en")


if (len(sys.argv) < 2):
	print("Please provide a domain/subdomain!")
	sys.exit(0)

elif (len(sys.argv[1]) > 30):
	print("Are you sure that's a domain?!")
	sys.exit(0)



def nmap_scan(target):

	print(cool_effect)
	print("\tNmap scan")
	print(cool_effect)


	time.sleep(3)

	type_of_connection, nmap_target = target.split("//")

	#scan using the ip
	nmap_target = socket.gethostbyname(nmap_target)
	
	print("Starting nmap scan on " + nmap_target + "\n\n")

	call('nmap -T4 -A -v -sV ' + nmap_target, shell=True)


	print("\n\nScanning dirs")

	time.sleep(5)

	dir_scan(target)



def dir_scan(target):
	#TODO: fix dir scanner issues for now just check for robots.txt


	#/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
	#wordlist_path = "/usr/share/wordlists/dirb/common.txt"

	#print("Scanning with wordlist -> " + wordlist_path)

	#call("gobuster -t 50 -w " + wordlist_path + " -u " + target, shell=True)
	print(cool_effect)
	print("\tGetting robots.txt if it exists...")
	print(cool_effect)


	call("curl " + target + "/robots.txt", shell=True)

	print("\n\nScanning security headers")

	time.sleep(5)

	security_headers_scan(target)



def security_headers_scan(target):

	shcheck_path = "~/Desktop/SecTools/shcheck.py"
	print(cool_effect)
	print("\tSecurity headers")
	print(cool_effect)


	call("python " + shcheck_path + " " + target + " -i -x", shell=True)


	print("Going to test for web app firewall (WAF)")

	time.sleep(5)

	waf_scan(target)



def waf_scan(target):

	print(cool_effect)
	print("\tWaf check")
	print(cool_effect)

	call("wafw00f " + target, shell=True)

	print("Good luck\nHappy hacking :)")


nmap_scan(sys.argv[1])
