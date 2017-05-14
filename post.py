from bs4 import BeautifulSoup
from markdown import markdown
from PIL import Image


class Post:
    def __init__(self, meta, content):
        self.meta = meta
        self.content = content

    def to_markdown(self):
        return markdown(self.content, extensions=['markdown.extensions.tables', 'markdown.extensions.fenced_code'])

    def amplify(self):
        html_doc = self.to_markdown()
        soup = BeautifulSoup(html_doc, 'html.parser')
        for img in soup.find_all('img'):
            img.name = 'amp-img'
            img['layout'] = 'responsive'
            try:
                if img['src'].startswith('/static/images'):
                    pil = Image.open('.' + img['src'])
                    width, height = pil.size
                    img['width'] = str(width) + "px"
                    img['height'] = str(height) + "px"
                else:
                    img['width'] = "240px"
                    img['height'] = "180px"
            except KeyError:
                pass
        return soup.prettify()

    def permanent_link(self):
        return '/{}/{}.html'.format(self.meta['date'].strftime('%Y/%m/%d'), self.meta['file_name'])

    def amp_link(self):
        return '/{}/{}.amp'.format(self.meta['date'].strftime('%Y/%m/%d'),
                                   self.meta['file_name'])
