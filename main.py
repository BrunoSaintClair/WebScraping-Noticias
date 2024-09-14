from Scraper import Scraper

scraper = Scraper()

url = 'https://www.nfl.com/news/'

texto = scraper.get_content(url, 'div', 'd3-o-media-object__body')
lista_noticias = scraper.extract_news(texto, 'h3')

scraper.show_news(lista_noticias)


# Outro exemplo de uso:

# url = 'https://ge.globo.com/'
# texto = scraper.get_content(url, 'div', 'feed-post-body')
# lista_noticias = scraper.extract_news(texto, 'a')
# scraper.show_news(lista_noticias)