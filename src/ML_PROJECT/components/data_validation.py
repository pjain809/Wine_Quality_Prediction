import pandas as pd
from ML_PROJECT import logger
from ML_PROJECT.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col in all_schema:
                    if data[col].dtype == self.config.all_schema[col]:
                        continue
                    else:
                        validation_status = False
                        break
                else:
                    validation_status = False
                    break

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation Status: {validation_status}")

            logger.info(f"Data Validation Status: {validation_status}")
            return validation_status

        except Exception as e:
            raise e
