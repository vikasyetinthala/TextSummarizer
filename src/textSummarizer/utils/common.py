import os 
from box.exceptions import BoxValueError 
import yaml 
from textSummarizer.logging import logger 
#from ensure import ensure_annotations 
from box import ConfigBox 
from pathlib import Path 
from typing import Any 



#@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """reads yaml file and returns 
    
    Args:
        path_to_yaml (str): path like input 

    Raises:
        ValueError: if yaml file is empty 
        e: empty file
    
    """
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file empty")
    except Exception as e:
        raise e 
    

#@ensure_annotations
def create_directories(path_to_directories:Path,verbose=True):
    """
    create the list of directories 

    Args:

        path_to_directory(list): list of path of directories
        verbose(bool, optional): ignore if multiple dirs is to be created. Default is False
    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}") 



#@ensure_annotations
def get_size(path:Path)->str:
    """
    get sze in KB  

    Args: 
        path(Path): path to get the size 

    return: 
        str: size in KB

    """
    size_in_kb=round(os.path.getsize(path)) 
    return f"~ {size_in_kb} KB"


if __name__=="__main__":
    pass