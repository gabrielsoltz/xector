import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import favicon

class URLModule():
    
    def __init__(self, url):
        self.url = url
        self.soup = bs(requests.get(self.url).content, "html.parser")
        self.images = self.get_images_urls()
        self.links = self.get_links()
        self.js = self.get_js()
        self.favicon = self.get_favicon()

    def is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    
    def get_images_urls(self):
        """
        Returns all image URLs on a single `url`
        """
        
        urls = []
        for img in tqdm(self.soup.find_all("img"), "Extracting images"):
            img_url = img.attrs.get("src")
            if not img_url:
                # if img does not contain src attribute, just skip
                continue
            
            # make the URL absolute by joining domain with the URL that is just extracted
            img_url = urljoin(self.url, img_url)
            try:
                pos = img_url.index("?")
                img_url = img_url[:pos]
            except ValueError:
                pass
        
            # finally, if the url is valid
            if self.is_valid(img_url):
                urls.append(img_url)
        
        return urls
    
    def get_links(self):
        links = []
        for link in tqdm(self.soup.findAll('a'), "Extracting links"):
            link = link.get('href')
            if self.is_valid(link):
                links.append(link)
        return links

    def get_js(self):
        js = [i.get('src') for i in self.soup.find_all('script') if i.get('src')] 
        return js

    def get_favicon(self):
        icons = favicon.get(self.url)
        return icons