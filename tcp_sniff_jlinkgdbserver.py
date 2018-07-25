# Author: Jacek Slimok
# Parser for JLingGDBServer SWO port TCP data

def handle_pair(data):
	tag = ord(data[0])
	#print "t: {} ({}), c: {} (0x{})".format(bin(tag), hex(tag), char, char.encode('hex'))
	num_chars = 0
	if (tag & 0x7) == 1:
		num_chars = 1
	elif (tag & 0x7) == 2:
		num_chars = 2
	elif (tag & 0x7) == 3:
		num_chars = 4
	else:
		print "Unknown tag: {}".format(hex(tag))
	if num_chars > 0:
		channel = (tag >> 3)
		print "[{}], c: {} (0x{})".format(channel, data[1:1+num_chars], data[1:1+num_chars].encode('hex'))
	return data[(1+num_chars):]

def parse(data):
	print "\n{}".format(data.encode('hex'))
	while len(data) > 0:
		data = handle_pair(data)