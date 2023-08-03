from pathlib import Path
from ML_PROJECT import logger
from ML_PROJECT.components.model_trainer import ModelTrainer
from ML_PROJECT.config.configuration import ConfigurationManager


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<\n\nx======================================x")
    except Exception as e:
        logger.exception(e)
        raise e
