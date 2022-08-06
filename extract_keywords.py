from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urlparse


class KeywordsProcessor:
    def __init__(self, url_container: list):
        self.url_container = url_container
        self.combined_df = pd.DataFrame()

    @staticmethod
    def get_content_from_website(soup: BeautifulSoup, attrs: dict = None):
        try:
            return soup.find('meta', attrs=attrs).get('content')
        except AttributeError:
            return ''

    @staticmethod
    def extract_keywords(keywords: str):
        return keywords.split(', ')

    def get_urls(self):
        for url in self.url_container:
            # get the name of the website - will be used as a file name with the keywords as result
            domain = urlparse(url).netloc
            website_name = domain.split('.')[1]

            # get the website information
            try:
                request = requests.get(url)
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
                print(f'Couldn\'t connect to {url}')
                continue

            # parse the website information
            soup = BeautifulSoup(request.content, 'lxml')

            # extract only relevant information from the website - keywords and description tags
            meta_tags_keywords = self.get_content_from_website(soup, {'name': 'keywords'})
            meta_tags_description = self.get_content_from_website(soup, {'name': 'description'})

            # split the keywords and description tags and have them in a list for the dataframes
            keywords = self.extract_keywords(meta_tags_keywords)
            description = self.extract_keywords(meta_tags_description)

            # create dataframes with the keywords to export them as csv file for later use
            keywords_df = pd.DataFrame({f'{website_name} keywords': keywords})
            description_df = pd.DataFrame({f'{website_name} description': description})

            # combine the two dfs and export the cleaned results
            self.combined_df = pd.concat(objs=[self.combined_df, keywords_df, description_df], axis=1)

        return self.combined_df
