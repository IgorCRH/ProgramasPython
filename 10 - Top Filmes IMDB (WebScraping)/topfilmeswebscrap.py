import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

try:
    url = 'https://www.imdb.com/chart/top/'
    resposta = requests.get(url, headers=headers)
    resposta.raise_for_status()
    soup = BeautifulSoup(resposta.text, "html.parser")
    print('Informacoes dos Filmes:')
    filmes = soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base").find_all('li')
    for filme in filmes:
        nomefilme = filme.find('h3',class_="ipc-title__text").text
        notafilme = filme.find('span',class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
        notafilme = notafilme.replace("IMDb rating:", "").strip()
        anofilme = filme.find('span',class_="sc-14dd939d-6 kHVqMR cli-title-metadata-item").text
        print('Nome:', nomefilme, 'Nota:', notafilme, 'Ano: ', anofilme)
except Exception as e:
    print(e)
