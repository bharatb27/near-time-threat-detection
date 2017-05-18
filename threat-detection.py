#!/bin/python
import sys, os, re
from geoip import geolite2

pattern = re.compile("^.*?\"\s+\"(.*?)\".*?(\d+\.\d+\.\d+\.\d+)\:(\d+).*?$")
def attack_checker(infile):
	if os.path.isfile(infile):
		for i, line in enumerate(open(infile)):
			for match in re.finditer(pattern, line):
				if match.group(1) == 'MATLAB R2013a':
					print "Yes, "+str(line)
				else:
					client_ip = match.group(2)
					match_ip = geolite2.lookup(client_ip)
					if str(match_ip.country) != 'IN':
						print "Yes, "+str(line)
					else:
						print "No, "+str(line)
	else:
		print "Log file does not found"
	
def main():
	file_path = raw_input("Please enter file path: ")
	attack_checker(file_path)	

if __name__ == "__main__":
	sys.exit(main())
