#!/usr/bin/python

import argparse, os, shutil

# Names of the output sub-directories and sizes of the images within them
ICON_TEMPLATES = {
	"mipmap-hdpi": 72,
	"mipmap-mdpi": 48,
	"mipmap-xhdpi": 96,
	"mipmap-xxhdpi": 144,
	"mipmap-xxxhdpi": 192
};

# Name of the output directory 'icon-font-to-png' produces 
EXPORT_DIR = "exported"

def main():
	parser = argparse.ArgumentParser(description='Converts Font Awesome icons to PNG files using \'icon-font-to-png\' to all Android icon formats. Replaces \'-\' with \'_\' in output file names.')
	parser.add_argument('icons', metavar='icon-name', type=str, nargs='+',
                   help='icon name without preceding \'fa-\'')
	parser.add_argument('--color', type=str, default="#000000",
                   help='color name or hex value (default: black - #000000)')
        parser.add_argument('--outdir', type=str, default="icon_export",
                   help='name of the output directory (default: icon_export)')

	args = parser.parse_args()

	# Delete output directory if exists
	if os.path.exists(args.outdir):
		shutil.rmtree(args.outdir)

	for dir, size in ICON_TEMPLATES.iteritems():
		print "Exporting icons of size " + str(size) + "x" + str(size) + " to: " + dir
		# Construct base of the command
		cmd = "icon-font-to-png --css font-awesome.css --ttf fontawesome-webfont.ttf"
		cmd = cmd + " --size " + str(size)
		cmd = cmd + " --color " + "\'" + args.color + "\'"

		# Add icons to the command
		for icon in args.icons:
			cmd = cmd + " " + icon

		# Execute conversion
		print cmd
		os.system(cmd)

		# Move all files created in this step to destination directory
		if os.path.exists(EXPORT_DIR):
			file_list = os.listdir(EXPORT_DIR)
			out_dir_base = args.outdir + "/" + dir + "/"
			if not os.path.exists(out_dir_base):
				os.makedirs(out_dir_base)
			for f in file_list:
				dst_file = f.replace("-", "_")
				src = EXPORT_DIR + "/" + f
				dst = out_dir_base + dst_file
				shutil.move(src, dst)

	# Delete file produced by 'icon-font-to-png'
	if os.path.exists(EXPORT_DIR):
		os.rmdir(EXPORT_DIR)

main()
