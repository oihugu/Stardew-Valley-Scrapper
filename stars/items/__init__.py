import os

#import all functions for every file in the folder
for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith('.py') and not file.startswith('__'):
        module = file[:-3]
        exec(f'from .{module} import *')