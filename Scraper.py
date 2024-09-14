import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Scraper:
    def __init__(self):
        pass

    def get_content(self, url, tag_html, element_class = None):
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'html.parser')
        
        if element_class is not None: 
            text = soup.find_all(tag_html, element_class)
        else:
            text = soup.find_all(tag_html) 
            
        return text

    def extract_news(self, text, title_tag, secondary_tag = None):
        news_list = []
        
        for news in text:
            title = news.find(title_tag)
            if secondary_tag is not None:
                secondary = news.find(secondary_tag)
            else:
                secondary = None
            
            if title is not None and secondary is not None:
                title = title.text.strip()
                secondary = secondary.text.strip()
            
                news = 'Titulo: ' + title + ', ' + secondary
                news_list.append(news)

            elif title is not None:
                title = title.text.strip()

                news = 'Titulo: ' + title
                news_list.append(news)

        return news_list

    def show_news(self, news_list):
        with open("noticias.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"Notícias extraídas em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}:" + "\n")
            arquivo.close()
            with open("noticias.txt", "a", encoding="utf-8") as arquivo:
                for news in news_list:
                    arquivo.write("\n" + news)
                arquivo.close()
