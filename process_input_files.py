import pandas as pd


class FileProcessor:
    def __init__(self, file_name: str):
        self.file_name = file_name

    '''
        top 20 websites of each category are extracted into csv files
        read the file and extract the urls
    '''

    def get_source_data(self) -> pd.DataFrame:
        source = pd.read_csv(self.file_name, index_col=False, encoding='cp1252')
        source.rename(columns=lambda x: x.strip(), inplace=True)

        source['Website'] = 'https://www.' + source['Website'].str.split().str[0]
        return source

    @staticmethod
    def get_website_urls(source: pd.DataFrame) -> list:
        return list(source['Website'].unique())

    def build_results(self) -> list:
        df = self.get_source_data()
        return self.get_website_urls(df)
