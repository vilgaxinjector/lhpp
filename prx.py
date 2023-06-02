import requests
from bs4 import BeautifulSoup

def scrape_proxies():
    # Danh sách các URL của các trang web cung cấp proxy miễn phí
    urls = [
        'https://www.free-proxy-list.net/',
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/anonymous-proxy.html',
        'https://free-proxy-list.net/',
        'https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=1',
        
    ]

    proxies = []

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')

            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                ip = columns[0].text
                port = columns[1].text
                proxy = f'{ip}:{port}'
                proxies.append(proxy)
        except requests.exceptions.RequestException:
            pass

    return proxies

proxy_list = scrape_proxies()

with open('proxies.txt', 'w') as file:
    for proxy in proxy_list:
        file.write(proxy + '\n')

print('Done > proxies.txt')
