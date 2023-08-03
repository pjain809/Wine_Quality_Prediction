from pathlib import Path
from ML_PROJECT import logger
from ML_PROJECT.components.data_transformation import DataTransformation
from ML_PROJECT.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Invalid Data Schema")
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
    except Exception as e:
        logger.exception(e)
        raise e
