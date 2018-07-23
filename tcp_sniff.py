#!/usr/bin/python2
# Author: Jacek Slimok
# Connects to specified TCP address and port and calls parser script.

import argparse, socket, importlib
from time import sleep

class ServerConnection():

	def __init__(self, host, port, parser):
		self.host = host
		self.port = port
		self.parser = importlib.import_module(parser)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.connect((host, port))

	def run(self):
		while True:
			data = self.server.recv(4096)
			if data:
				try:
					reload(self.parser)
					self.parser.parse(data)
					#print "{}".format(data.encode('hex'))
				except Exception as e:
					print e

def main():
	parser = argparse.ArgumentParser(description='Connects to specified TCP address and port and calls parser script.')
	parser.add_argument('parser', metavar='parser-script', type=str,
		help='parser script without file extension, must contain \'parse\' function')
	parser.add_argument('-i', '--ip', '--host', type=str, default="localhost",
		help='host to connect to (default: \'localhost\')')
	parser.add_argument('-p', '--port', type=int, help='port to connect to', required=True)
	args = parser.parse_args()

	while True:
		try:
			connection = ServerConnection(args.ip, args.port, args.parser)
			connection.run()
		except Exception as e:
		 	# Failed to connect, connection closed or other error
		 	# Sleep for 1s and reattempt
		 	print e
		 	sleep(1)

main()