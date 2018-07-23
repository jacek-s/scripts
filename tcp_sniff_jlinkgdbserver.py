# Author: Jacek Slimok
# Parser for JLingGDBServer SWO port TCP data

def handle_pair(data):
	tag = ord(data[0])
	char = data[1]
	#print "t: {} ({}), c: {} (0x{})".format(bin(tag), hex(tag), char, char.encode('hex'))
	if (tag & 0x7) != 0x1:
		print "Unknown tag: {}".format(hex(tag))
	else:
		channel = (tag >> 3)
		print "[{}], c: {} (0x{})".format(channel, char, char.encode('hex'))
	return data[2:]

def parse(data):
	print "\n{}".format(data.encode('hex'))
	while len(data) > 0:
		data = handle_pair(data)