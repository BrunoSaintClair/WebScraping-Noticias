import requests
from bs4 import BeautifulSoup

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
        for news in news_list:
            print(news)
            print('*' * 60)
