#!/usr/bin/python

import time
import sys
from subprocess import call

print("\nBug bounty enumeration\n\n")


if (len(sys.argv) < 2):
	print("Please provide a domain/subdomain!")
	sys.exit(0)

elif (len(sys.argv[1]) > 30):
	print("Are you sure that's a domain?!")
	sys.exit(0)

#TODO: check if it contains https/http in the url



def nmap_scan(target):
	#TODO: take https/http of target string for nmap to work
	print("Starting nmap scan on " + target + "\n\n")

	call('nmap -T4 -A -v -sV ' + target, shell=True)

	print("\n\nScanning dirs")
	time.sleep(5)
	dir_scan(target)

def dir_scan(target):
	#TODO: fix dir scanner issues for now just check for robots.txt


	#/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
	#wordlist_path = "/usr/share/wordlists/dirb/common.txt"

	#print("Scanning with wordlist -> " + wordlist_path)

	#call("gobuster -t 50 -w " + wordlist_path + " -u " + target, shell=True)

	call("curl " + target + "/robots.txt", shell=True)

	print("\n\nScanning security headers")
	time.sleep(5)
	security_headers_scan(target)

def security_headers_scan(target):
	shcheck_path = "~/Desktop/SecTools/shcheck.py"

	call("python " + shcheck_path + " " + target + " -i -x", shell=True)

	print("Going to test for web app firewall (WAF)")
	time.sleep(5)
	#waf_scan(target)




nmap_scan(sys.argv[1])
