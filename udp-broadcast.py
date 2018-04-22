#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Łukasz Marcińczak
# date: 2018-04-21

import sys
import socket
import os
import subprocess


def help():
	print("\nUżycie:")
	print("{} -ip=<adres ip> -p=<port>\n".format(sys.argv[0]))
	print("\t--address_ip lub -ip - adres ip (domyślnie: 255.255.255.255)")
	print("\t--port\t     lub -p  - port\t(domyślnie: 1234)\n")

def main(argv):
	ip = "255.255.255.255"
	port = 1234
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
				port = int(temp[1])
			except IndexError:
				print("Niepoprawny argument: --port (-p)")
				sys.exit()
		else:
			print("Niepoprawny argument")
			sys.exit()
	
	print("Streaming at IP {}, PORT {}".format(ip, port))
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	pipe_r, pipe_w = os.pipe()
	process = subprocess.Popen(["ffmpeg", "-re", "-video_size", "1920x1080", "-framerate", "30", "-f", "x11grab", "-i", ":0.0", "-c:v", "mpeg2video", "-crf", "0", "-preset", "ultrafast", "-maxrate", "20M", "-b:v", "10M", "-f", "mpegts", "-"], stdout=pipe_w)
	#print(process.comunicate()[0])
	data = os.fdopen(pipe_r)
	message = data.read()
	while 1: # główna pętla programu
		sock.sendto(message, (ip, port)) # wysyłanie datagramu UDP


if __name__ == "__main__":
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print("Program zakończony przez urzytkownika!")

