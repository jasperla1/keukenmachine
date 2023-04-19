import requests
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool


st = time.time()
urls = []
for i in range(15):

    # Make a request to the recipe
    url = "https://www.ah.nl/allerhande/recept/R-R" + str(1198231 + i)
    response = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Scrape the ingredients list
    if "staafmixer" in soup.get_text().lower():
    #if "staafmixer" in str(soup.find_all("div", {"class": "recipe-preparation-steps_root__5khrn"})).lower():
        urls.append(url)
        print(url)
print(urls)
et = time.time()
print(et-st)




