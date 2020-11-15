import requests
from bs4 import BeautifulSoup
from lxml import html
import shutil
import os

def main() -> None:
    url = "website"

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    print("Started...")

    with requests.Session() as s:
        page = s.get(url, headers=headers).text
        soup = BeautifulSoup(page, 'lxml')

        file = [ dl.a['href'].split('/')[-1] for dl in soup.find_all("td", class_="fb-n") ]
        # pop first of array because it was for file browsing stuff .. and \n
        file.pop(0)
        file.pop(0)
        
        # Stalled for some reason earlier this was used to remove every file i had already downloaded
        # for i in file:
        #     if not i == "file.txt":
        #         file.pop(0)

        print(file)
        for f in file:
            with s.get(url + f, stream=True) as r:
                with open(os.getcwd() + "\\download\\" + f, 'wb') as file:
                    print(f"download started for {f}")
                    shutil.copyfileobj(r.raw, file)
                    print(f"download complete")


if __name__ == "__main__":
    main()