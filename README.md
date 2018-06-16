# Cookiecutter Chemios

This is a template for chemios instrument drivers.  Each driver is for a type of instrument (e.g., pumps, temperature controllers, etc.).

This repository is a [cookiecutter](https://github.com/audreyr/cookiecutter) template, which means it allows you to fill out a qucik command line form to generate a pre-scaffolded repo for your driver.

## Structure of a Chemios Driver

Each chemios driver contains a base.py file.  This file contains an [abstract base class](https://www.python-course.eu/python3_abstract_classes.php) that models the interface of all instruments of that type.

Take the temperature controlller driver, for example:

    chemios_tc/
        __init__.py
        chemios_tc_base.py #Contains base class for temperature controllers
        cli.py #Commnad line interface file
        utils.py #Utilities
    .github  #Template for pull requests



## Installation

This assumes you have [python 3.0 or above](https://www.python.org/downloads/) and git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed.

1. Install cookiecutter using pip:

    pip install -U cookiecutter

2. To create a new cookiecutter, run the following commands.  You will be prompted at the command line for information needed to create the new driver repository.

    $  cookiecutter https://github.com/Chemios/cookiecutter-chemios
    $  cookiecutter cookiecutter-chemios

3. Once you've created the repository, change into the directory and initialize git:

    $ git init
    $ git add -A
    $ git commit -am "Initial Commit"

4. Then create a new repository on github (without a license or readme) and copy the https link.  Run the following command at your command line:

    $ git remote add origin <link_to_repository>
    $ git push -u origin master

Now your driver is ready to use and synced to github.

