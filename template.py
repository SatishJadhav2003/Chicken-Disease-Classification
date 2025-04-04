# this file is use to create the directory structure and files for the project

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:- %(message)s:')

project_name = "cnnClassification"

list_of_files = [
".github/workflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/utils/__init__.py",
f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/constants/__init__.py",
"config/config.yaml",
"dvc.yaml",
"params.yaml",
"requirements.txt",
"setup.py",
"reasearch/trials.ipynb",
]


for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} already exists.")