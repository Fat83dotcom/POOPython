import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url: str, title: str, body: str) -> None:
        self.url = url
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'''
        Url: {self.url}
        Title: {self.title}
        Body: {self.body}
        '''


class WebSite:
    def __init__(
        self,
        name: str,
        url: str,
        titleTag: str,
        bodyTag: str
    ) -> None:
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj: BeautifulSoup, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selectedElems]
            )
        return ''

    def parse(self, site, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                print(content)


if __name__ == '__main__':
    crawler = Crawler()
    siteData: list = [
        [
            'Estação',
            'https://www.brainstormtecnologia.tech',
            'h1',
            'div.container'
        ]
    ]

    webSites: list = []
    for row in siteData:
        webSites.append(
            WebSite(row[0], row[1], row[2], row[3])
        )

    crawler.parse(
        webSites[0], 'https://www.brainstormtecnologia.tech'
    )
