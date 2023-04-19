import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_links(url="https://www.ah.nl/allerhande/recepten-zoeken", links=[], pages=[]):
    r = requests.get(url)
    print(r.url, flush=True)
    pages.append(url)
    soup = BeautifulSoup(r.text, "html.parser")
    next_pages = soup.select("a.pagination_pageAnchor__6fH-n")
    for link in soup.select("a.display-card_root__o17AY"):
        links.append(urljoin(url, link.get("href")))

    for i in next_pages:
        next_page = urljoin(url, i.get("href"))
        if next_page not in pages:
            pages.append(next_page)
            return fetch_links(next_page, links, pages)

    return links

def refresh_links():
    links = fetch_links()
    with open('links.csv', 'w') as f:
        for link in links:
            f.write(link + '\n')




refresh_links()


