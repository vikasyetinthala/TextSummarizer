from textSummarizer.constants import CONFIG_FILE_PATH,PARAM_FILE_PATH
from textSummarizer.utils.common import *
from textSummarizer.entity import DataIngestionConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAM_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)

        create_directories([self.config.artifacts_root,self.config.data_ingestion.root_dir])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion 
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config 
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation 
        create_directories([config.root_dir])

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config 
