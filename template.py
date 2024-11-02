import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [



    # The Project source file countain these elements 

    f"{project_name}/__init__.py",



     # list of All components Files 

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",



    # List of configuration Of Connection files  
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/configuration/mongodb_connection.py",


    # list of constants 
# 
    f"{project_name}/constants/__init__.py",


    # list of entity files 

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",


    # Exception handling Custom 
    f"{project_name}/exception/__init__.py",

    # Event logger 
    f"{project_name}/logger/__init__.py",


    # Pipelines 
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",


    # Common files (utils)
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",




    # notebook Exxperiment 
    "notebook/experiment1.ipynb",
    "notebook/experiment2.ipynb",



    # Config files 
    "config/model.yaml",   # for Hyperparameter tunning using Neuro mf
    "config/schema.yaml",   # for data valisation 



    # CICD
    ".github/workflows/AWS_CICD.yaml",



    # Files withod any folder 
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "README.md",
    ".gitignore",
    ".env",


]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")



