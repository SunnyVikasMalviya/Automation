#! python3
# backupToZip.py    - Copies an entire folder and its contents into a zip
# file whose filename increments.

import zipfile, os

def backupToZip(folderpath):
    # Backup contents of the given folder path into a Zip file.

    folder = os.path.abspath(folderpath)

    # Check existing files for latest increment number
    num = 1
    while True:
        zipFilename = "{}_{}.zip".format(os.path.basename(folder), str(num))
        if not os.path.exists(zipFilename):
            break
        num += 1
    
    # Create the zip file
    print("Creating {}...".format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, "w")

    # Add the subfolders and files in the given folderpath
    for parent, children, files in os.walk(folderpath):
        print("Adding files in {}...".format(parent))
        backupZip.write(parent)

        # Add all the files in this folder to the zip file.
        for file in files:
            newBase = os.path.basename(folderpath) + "_"
            if file.startswith(newBase) and file.endswith(".zip"):
                continue        # Don't backup the zip files
            backupZip.write(os.path.join(parent, file))
    backupZip.close()
    print("Done. Thanks for your patience!")

if __name__ == "__main__":
    folderpath = "V:\MVik\Projects\Morganize"
    backupToZip(folderpath)