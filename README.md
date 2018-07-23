
# Scripts
## android_fa_convert.py

Converts [Font Awesome](http://fontawesome.io/) icons to PNG in all Android sizes and places them in their respective directories: "mipmap-mdpi" for 48,48px, mipmap-hdpi" for 72x72px etc. Replaces '-' with '_' in output file names.

### Usage:
```
usage: android_fa_convert.py [-h] [--color COLOR] [--outdir OUTDIR]
                             icon-name [icon-name ...]

Converts Font Awesome icons to PNG files using 'icon-font-to-png' to all
Android icon formats. Replaces '-' with '_' in output file names.

positional arguments:
  icon-name        icon name without preceding 'fa-'

optional arguments:
  -h, --help       show this help message and exit
  --color COLOR    color name or hex value (default: black - #000000)
  --outdir OUTDIR  name of the output directory (default: icon_export)
```
Convert single icon using default color:
`./android_fa_convert.py pie-chart`

Convert multiple icons using default color:
`./android_fa_convert.py pie-chart share-alt umbrella`

Convert single icon and output in blue color:
`./android_fa_convert.py --color blue pie-chart`

Convert single icon and output in hex-encoded blue (#0000FF) color:
`./android_fa_convert.py --color "#0000FF" pie-chart`

### Requirements:
python, [icon-font-to-png](https://github.com/Pythonity/icon-font-to-png)

## tcp_sniff.py

Connects to specified TCP address and port and calls parser script while sniffing all incoming traffic. Sniffer script is hot-reloaded, allowing live analysis without having to restart the script. Script attempts to re-connect to server if the connection is dropped.

### Usage:
```
usage: tcp_sniff.py [-h] [-i IP] -p PORT parser-script

Connects to specified TCP address and port and calls parser script.

positional arguments:
  parser-script         parser script without file extension, must contain
                        'parse' function

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP, --host IP
                        host to connect to (default: 'localhost')
  -p PORT, --port PORT  port to connect to
```
Run a `tcp_sniff_jlinkgdbserver` script:
`./tcp_sniff.py -p 2332 tcp_sniff_jlinkgdbserver`

## tcp_sniff_jlinkgdbserver.py

Parser script used in conjuction with `tcp_sniff.py`. Analyzes network traffic on SWO port for JLinkGDBServer.