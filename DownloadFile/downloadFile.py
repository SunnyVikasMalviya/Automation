import requests
import os

def downloadFile(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
        file = open("RomeoAndJulient.txt", "wb")
        filepath = os.path.abspath(file)
        for chunk in res.iter_content(1024):
            file.write(chunk)
        file.close()
        return filepath
    except Exception as exc:
        print("There was a problem while downloading content from given url {}.\nError code: {}".format(url, exc))
        return ""
if __name__ == "__main__":
    url = "https://www.automatetheboringstuff.com/files/rj.txt"
    print(downloadFile(url))
    
