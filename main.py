from Scraper import Scraper

url = 'https://www.nfl.com/news/'

scraper = Scraper()

texto = scraper.get_content(url,'div', 'd3-o-media-object__body')
lista_noticias = scraper.extract_news(texto, 'h3', 'p')

print()
print('Notícias da NFL: ')
print()
scraper.show_news(lista_noticias)



url = 'https://www.nba.com/'

texto = scraper.get_content(url, 'h3', 'Text_text__I2GnQ ContentSlide_text__m_W0K')

lista_noticias = scraper.extract_news(texto, 'span', 'MultiLineEllipsis_ellipsis___1H7z')

print()
print('Notícias da NBA: ')
print()
scraper.show_news(lista_noticias)



url = 'https://ge.globo.com/'

texto = scraper.get_content(url, 'div', 'feed-post-body')

lista_noticias = scraper.extract_news(texto, 'a')

print()
print('Notícias do GE: ')
print()
scraper.show_news(lista_noticias)