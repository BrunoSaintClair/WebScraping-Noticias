from Scraper import Scraper

url = 'https://www.nfl.com/news/'

scraper = Scraper()

texto = scraper.get_content(url,'div', 'd3-o-media-object__body')
lista_noticias = scraper.extract_news(texto, 'h3', 'p')

scraper.show_news(lista_noticias)