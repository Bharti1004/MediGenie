# here we will design the entire project structure

import os
from pathlib import Path
import logging  #inbuilt package in python & also log the info in my terminal

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')  #format gives format of log msg
# [%(asctime)s] = shows the time and  %(message)s = shows the log message you want to show
 
 
#list of files we are including in our project 
list_of_files = [
    "src/__init__.py",   #it is my constructor file
    "src/helper.py",     # here we write all the functionality
    "src/prompt.py",
    ".env",
    "setup.py",  # kyunki hmne upr vaali sarai files local package me download krni h
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   #here we use path kyunki kuch system / slash use krte h aur kuch \ slash
    filedir, filename = os.path.split(filepath)  #yha pr filedir me hmara foldername aayega

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")   # (when I run this code,it will create
                                                   # all the folders and files automatically)
                                                   
# in future , if we want more folders or files, then simply add them in above code &run it                                                 