#! python3
# renameDates.py - Renames filenames with American dates format(MM-DD-YYYY)
# to European date format(DD-MM-YYYY)

import os
import re
import shutil

datePattern = re.compile(r"""^(.*?)             # before date
                         ((0|1)?\d)-            # month
                         ((0|1|2|3)?\d)-      # date
                         ((19|20)\d\d)          # year
                         (.*?)$                 # after date
                         """, re.VERBOSE)

def renameDates(folderPath):
    for usFilename in os.listdir(folderPath):
        # Creating match object
        mo = datePattern.search(usFilename)
        if mo == None:
            continue

        # Get the different parts of the filename from match object
        before = mo.group(1)
        month = mo.group(2)
        date = mo.group(4)
        year = mo.group(6)
        after = mo.group(8)

        euroFileName = before + date + "-" + month + "-" + year + after
        # euroFileName = "{}{}-{}-{}{}".format(before, date, month, year, after)

        # Creating absolute file paths
        workingDirectory = os.path.abspath(folderPath)
        usFilepath = os.path.join(workingDirectory, usFilename)
        euroFilepath = os.path.join(workingDirectory, euroFileName)

        # Updating date format in filenames
        print("Renaming {} to {}".format(usFilename, euroFileName))
        shutil.move(usFilepath, euroFilepath)

if __name__ == "__main__":
    folderPath = "V:\\MVik\\Projects\\Python Automation Projects\\RenameDateFiles"
    print("Renaming files with us date format to euro date format in folder {}.".format(os.getcwd()))
    renameDates(folderPath)
