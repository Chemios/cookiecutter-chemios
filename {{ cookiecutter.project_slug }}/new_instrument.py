'''
Create a new instrument in the current instrument type

Usage:
    new_instrument.py INSTRUMENT_NAME

Arguments:
    INSTRUMENT_NAME Name of new instrument
Options:
    -h --help Show this screen
'''
import os
from {{cookiecutter.project_slug}}.utils import package_path
from shutil import copyfile
from fileinput import FileInput
from docopt import docopt

def new_instrument(instrument_name):
    '''Create a new instrument based on the base files'''
    #Change to {{cookiecutter.project_slug}} directory and copy base file
    working_path = package_path()
    old_path = os.getcwd()
    os.chdir(working_path)

    #Create new filename
    if instrument_name.rstrip('.py') == instrument_name:
        instrument_name = instrument_name.rstrip('.py')
    instrument_filename = '_' + instrument_name.lower().replace(' ','_').replace('-', '_') + '.py'
    copyfile('{{cookiecutter.project_slug}}_base.py', instrument_filename)

    #Open the file and change the import statement and the name of the class
    class_name = instrument_name.title().replace(' ', '') + '(TemperatureControllers)'
    with FileInput(instrument_filename, inplace=True) as file:
        for line in file:
            print(line.replace('TemperatureControllers(ABC)', class_name).replace('from abc import ABC', 'from .{{cookiecutter.project_slug}}_base import TemperatureControllers'),
                  end='')

    #Add class to package level in __init__.py
    import_statement = "from .{} import {}".format(instrument_filename.rstrip('.py'),
                                                   instrument_name.title().replace(' ', ''))
    with open('__init__.py', 'a') as f:
        f.write(import_statement)

    #Change back to the original directory
    os.chdir(old_path)

args = docopt(__doc__)
if args['INSTRUMENT_NAME']:
    new_instrument(args['INSTRUMENT_NAME'])
