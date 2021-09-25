import requests
import bs4

def search(query):
    response = requests.get("https://www.xvideos.com/?k=" + query)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    data = []
    deck = soup.find_all(class_="thumb-block")
    for card in deck:
        try:
            info = {
                "urls": ("https://www.xvideos.com/" + str(card).split('<a href="')[1].split('">')[0]),
                "imgs": (str(card).split('data-src="')[1].split('.jpg')[0] + ".jpg"),
                "titles": (str(card).split('title="')[1].split('">')[0])
            }
            data.append(info)
        except IndexError:
            pass

    return data

