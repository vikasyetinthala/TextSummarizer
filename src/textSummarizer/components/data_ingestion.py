from urllib import request 
from zipfile import ZipFile
from textSummarizer.entity import DataIngestionConfig 
from textSummarizer.logging import logger
import os


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config 

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
           
            filename,headers=request.urlretrieve(url=self.config.source_url,filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"file already exists")

    def extract_zip_file(self):
        """
        zip_file_path: str 
        extract zip file into the data directory 
        function return None 
        """
        unzip_path=self.config.unzip_dir 
        os.makedirs(unzip_path,exist_ok=True)
        with ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)