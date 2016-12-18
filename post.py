from markdown import markdown


class Post:
    def __init__(self, meta, content):
        self.meta = meta
        self.content = content

    def to_markdown(self):
        return markdown(self.content, extensions=['markdown.extensions.tables'])

    def link(self):
        return '{}/{}.html'.format(self.meta['date'].strftime('%Y/%m/%d'), self.meta['file_name'])
