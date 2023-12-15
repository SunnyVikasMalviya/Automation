#! python3
# mapIt.py  - Launches a map in the browser using an address form
# the command line or clipboard.

import webbrowser
import sys
import pyperclip

def mapit():
    """
    mapIt.py  - Launches a map in the browser using an address form
    the command line or clipboard.
    """
    # Get address from command line.    
    if len(sys.argv) > 1:
        address = " ".join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    webbrowser.open("https://www.google.com/maps/place/{}".format(address))

if __name__ == "__main__":
    mapit()

    