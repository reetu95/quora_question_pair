import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

project_name = "Quora"

list_of_files = [
    "requirements.txt",
    "setup.py",
    f'src/__init__.py',
    f'src/components/__init__.py',
    f'src/components/data_ingestion.py',
    f'src/components/data_transformation.py',
    f'src/components/model_tariner.py',
    f'src/pipeline/__init__.py',
    f'src/pipeline/train_pipeline.py',
    f'src/pipeline/predict_pipeline.py',
    f'src/logger.py',
    f'src/exception.py',
    f'src/utils.py',
    f'notebook/EDA.ipynb',
    f'notebook/model_trainer.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        if not os.path.exists(filedir):
            os.makedirs(filedir)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
