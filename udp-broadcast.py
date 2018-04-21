#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Łukasz Marcińczak
# date: 2018-04-21

import sys
import socket


def help():
	print("\nUżycie:")
	print("{} -ip=<adres ip> -p=<port>\n".format(sys.argv[0]))
	print("\t--address_ip lub -ip - adres ip")
	print("\t--port\t     lub -p  - port\n")

def main(argv):
	ip = ""
	port = 0
	if len(argv) == 1:
		help()
		sys.exit()
	
	argumenty = argv[1:]
	for i in range(len(argumenty)):
		if (argumenty[i] == "--help") or (argumenty[i] == "-h"):
			help()
			sys.exit()
		elif (argumenty[i][:12] == "--address_ip") or (argumenty[i][:3] == "-ip"):
			temp = argumenty[i].split("=")
			try:
				ip = temp[1]
			except IndexError:
				print("Niepoprawny argument: --address_ip (-ip)")
				sys.exit()
		elif (argumenty[i][:6] == "--port") or (argumenty[i][:2] == "-p"):
			temp = argumenty[i].split("=")
			try:
				port = temp[1]
			except IndexError:
				print("Niepoprawny argument: --port (-p)")
				sys.exit()
		else:
			print("Niepoprawny argument")
			sys.exit()
	
	print(ip, port)


if __name__ == "__main__":
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print("Program zakończony przez urzytkownika!")

