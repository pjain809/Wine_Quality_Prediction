import os
import yaml
import json
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ML_PROJECT import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads YAML File and returns ValueError if empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML File:  {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML File is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a List of Directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves JSON Data
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON File saved at - {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON File's Data
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON Data Loaded Successfully from - {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves Binary File
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary File Saved at - {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load Binary File's Data
    """
    content = joblib.load(path)
    logger.info(f"Binary File Loaded from - {path}")
    return content


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get Size in KB
    """
    size = round(os.path.getsize(path)/1024)
    return f"~ {size}KB"
