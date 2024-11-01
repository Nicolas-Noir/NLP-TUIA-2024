import requests
from bs4 import BeautifulSoup

url = "https://tableros.yvera.tur.ar/"

response = requests.get(url, verify=False).text
soup = BeautifulSoup(response, 'html.parser')

primeros_div = soup.find_all('div', {'class':'card bg-transparent m-0 border-0 collapse.show bs4cards-blahblahblah bs4cards-Todos bs4cards-Tablero'})

for div in primeros_div:
    if div.find('a', {'href':'https://tableros.yvera.tur.ar/tablero_ODS'}):
      segundo_div = div.find('div', {'class':'card-body'})
      print(segundo_div.find('p').text)
