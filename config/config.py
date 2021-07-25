import sys
import os
sys.path.insert(0,os.getcwd())

from datetime import datetime

import json
import base64

class Config:
    default = {
        "fileDir": os.getcwd(),
        "script_dir" : os.path.abspath(''),
        "args" : sys.argv,
        "dateDay" : datetime.now().strftime("%d-%m-%Y"),
        "dateDayHourMin": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }