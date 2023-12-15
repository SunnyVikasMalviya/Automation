#! python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage : python <mcb.py file path> <keyword>       - Loads keyword text to clipboard.
#       : python <mcb.py file path> list            - Loads all keywords to clipboard.
#       : python <mcb.py file path> clear           - Clears the list of saved keywords.
#       : python <mcb.py file path> save <keyword>  - Saves clipboard to keyword.
#       : python <mcb.py file path> del <keyword>   - Deletes keyword from list.

import shelve       # To manage storage of clipboard and respective texts
import pyperclip    # To manage clipboard operations
import sys          # To manage command line arguments

def multiClipboard():
    # Creating a shelf file
    mcbShelfFile = shelve.open("mcb")

    # Saving keywords
    if len(sys.argv) == 3:
        if sys.argv[1].lower() == "save":
            mcbShelfFile[sys.argv[2]] = pyperclip.paste()       # Saving Keyword
        elif sys.argv[1].lower() == "del":
            del mcbShelfFile[sys.argv[2]]                       # Delete keyword
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == "clear":
            mcbShelfFile.clear()                                # Clear keywords
        elif sys.argv[1].lower() == "list":
            pyperclip.copy(str(list(mcbShelfFile.keys())))      # List Keywords
        else:
            pyperclip.copy(mcbShelfFile[sys.argv[1]])           # Loading keyword text

    # Closing shelf File
    mcbShelfFile.close()

if __name__ == "__main__":
    multiClipboard()