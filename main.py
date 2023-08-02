from ML_PROJECT import logger
from ML_PROJECT.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ML_PROJECT.pipeline.stage02_data_validation import DataValidationTrainingPipeline


# Data Ingestion
STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
except Exception as e:
    logger.exception(e)
    raise e


# Data Validation
STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
except Exception as e:
    logger.exception(e)
    raise e
