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

    def extract_news(self, text, title_tag, date_tag):
        news_list = []
        
        for news in text:
            title = news.find(title_tag)
            date = news.find(date_tag)
            
            if title is not None and date is not None:
                title = title.text.strip()
                date = date.text.strip()
            
                news = 'Titulo: ' + title + ', data: ' + date
                news_list.append(news)

        return news_list

    def show_news(self, news_list):
        for news in news_list:
            print(news)
            print('*' * 60)
