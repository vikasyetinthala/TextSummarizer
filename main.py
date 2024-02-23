from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from textSummarizer.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger 

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline () 
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed  <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation=DataTransformationTrainingPipeline() 
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed  <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e