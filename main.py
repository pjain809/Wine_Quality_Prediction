from ML_PROJECT import logger
from ML_PROJECT.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ML_PROJECT.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from ML_PROJECT.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from ML_PROJECT.pipeline.stage04_model_trainer import  ModelTrainingPipeline

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


# Data Transformation
STAGE_NAME = "Data Transformation"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
except Exception as e:
    logger.exception(e)
    raise e


# Model Training
STAGE_NAME = "Model Training"

try:
    logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
except Exception as e:
    logger.exception(e)
    raise
