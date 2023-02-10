from bs4 import BeautifulSoup as soup
import requests


def main(url):
    response = requests.get(url)
    page_soup = soup(response.text, "html.parser")

    print(page_soup)

if __name__ == '__main__':
    # headers, cookies = hd()
    url = 'https://ddfe.blazejbucha.com/models/SRTM2gravity2018/data/'

    main(url)