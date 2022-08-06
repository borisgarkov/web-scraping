import pandas as pd
from process_input_files import FileProcessor
from extract_keywords import KeywordsProcessor

sports_urls: list = FileProcessor(file_name='sports_websites.csv').build_results()
sports_final_data: pd.DataFrame = KeywordsProcessor(url_container=sports_urls).get_urls()
sports_final_data.to_csv(f'sport_websites_keywords.csv', index=False)

tv_streams_urls: list = FileProcessor(file_name='tv_streams_websites.csv').build_results()
tv_streams_final_data: pd.DataFrame = KeywordsProcessor(url_container=tv_streams_urls).get_urls()
tv_streams_final_data.to_csv('tv_streams_keywords.csv', index=False)

file_sharing_hosting_urls: list = FileProcessor(file_name='file_sharing_hosting_websites.csv').build_results()
file_sharing_hosting_final_data: pd.DataFrame = KeywordsProcessor(url_container=file_sharing_hosting_urls).get_urls()
file_sharing_hosting_final_data.to_csv('file_sharing_hosting_keywords.csv', index=False)
