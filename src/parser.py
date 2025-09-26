from bs4 import BeautifulSoup

from src.base_input import BaseInput
from src.base_output import BaseOutput
from src.news_model import NewsModel


class Parser:
    def __init__(self, inp: BaseInput, out: BaseOutput):
        self.input = inp
        self.output = out

    def parse_news(self, limit: int | None = None):
        max_count = None
        count = 0
        while True:
            result_page = []
            html = self.input.fetch()
            soup = BeautifulSoup(html, 'html.parser')
            if max_count is None:
                max_count = max([int(i.text) for i in soup.find("div", attrs={"class": "modern-page-navigation"}).find_all("a") if i.text.isdigit()])
            print(f"⚒️ Страница {self.input.page}/{max_count}")
            lst_tag = soup.find('div', attrs={'class': 'news-list'})
            items_tag = lst_tag.find_all('div', attrs={'class': 'news-item'})
            for i, item in enumerate(items_tag):
                print(f"⭐ Новость {i+1}/{len(items_tag)}")
                try:
                    image = item.find('img').attrs['src']
                except AttributeError:
                    image = None
                header_tag = item.find('h3', attrs={'class': 'news-item-header'})
                title = header_tag.find("a").text
                description = item.find("div", attrs={"class": "news-item-text"}).text.replace(title, "").strip()
                date = item.find('div', attrs={'class': 'news-item-date'}).text
                url = header_tag.find('a').attrs['href']
                news_id = url.split('/')[-2]
                self.input.set_page_id(news_id)
                content_html = self.input.fetch_page()
                model = NewsModel(
                    title=title,
                    description=description,
                    url=url,
                    date=date,
                    cover_url=image,
                    content_html=content_html
                )
                result_page.append(model)
                count += 1
                if limit is not None and count >= limit:
                    self.output.save_many(result_page)
                    return
            self.output.save_many(result_page)
            if len(soup.find_all("a", {"class": "modern-page-next"})) == 0:
                break
            self.input.next_page()
