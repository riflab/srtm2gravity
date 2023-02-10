from bs4 import BeautifulSoup as soup
import requests
import re

def parse_url(url):
    response = requests.get(url)
    page_soup = soup(response.text, "html.parser")
    page = page_soup.find_all('a', href=True)

    list = [item['href'] for item in page]

    return list

def download_file(url, path):
    response = requests.get(url)
    open(path, "wb").write(response.content)

def main(url):
    
    pages_1 = parse_url(url)[-2:]
    
    for i in pages_1:
        url_1 = url + i
        print(' > ' + url_1)

        pages_2 = parse_url(url_1)

        for j in pages_2[5:]:
            url_2 = url_1 + j
            print(' >> ' + url_2)

            pages_3 = parse_url(url_2)

            for k in pages_3[5:]:
                url_3 = url_2 + k
                # print(' >>> ' + url_3)
                path = 'data/' + i + k
                print(path)
                download_file(url_3, path)

if __name__ == '__main__':
    # headers, cookies = hd()
    url = 'https://ddfe.blazejbucha.com/models/SRTM2gravity2018/data/'

    main(url)