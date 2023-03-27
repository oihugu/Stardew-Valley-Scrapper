import os
import sys

#import all files in the stars directory
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py"):
        __import__(file[:-3])
        
