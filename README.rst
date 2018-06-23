.. image:: https://travis-ci.com/Chemios/cookiecutter-chemios.svg?branch=master
    :target: https://travis-ci.com/Chemios/cookiecutter-chemios
    :alt: Build status on Travis CI

.. image:: https://readthedocs.org/projects/cookiecutter-chemios/badge
    :target: https://cookiecutter-chemios.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter Chemios
====================

This is a template for chemios_ instrument drivers.
Each driver is for a type of instrument (e.g., pumps, temperature controllers, etc.).

This repository is a cookiecutter_ template.
So, you fill out a quick command line form to generate a pre-scaffolded repo for your driver.

.. _chemios:  https://github.com/Chemios/chemios
.. _cookiecutter: https://github.com/audreyr/cookiecutter

Below are some basic instructions to get you started.  You can find more detailed documenation here_.

.. _here: https://cookiecutter-chemios.readthedocs.io/en/latest/

Structure of a Chemios Driver
-----------------------------

Each chemios driver contains a base.py file.
This file contains an `abstract base class`_ that models the interface of all instruments of that type.

Take the temperature controlller driver, for example:

.. code-block:: bash

    chemios_tc/
        __init__.py
        chemios_tc_base.py #Contains base class for temperature controllers
        cli.py #Commnad line interface file
        utils.py #Utilities
    .github  #Template for pull requests

.. _`abstract base class`: https://www.python-course.eu/python3_abstract_classes.php

Installation
------------

This assumes you have `python 3.0 or above`_ and git_ installed.

1. Install cookiecutter using pip:

    .. code-block:: bash

        pip install -U cookiecutter

2. To create a new cookiecutter, run the following commands.  You will be prompted at the command line for information needed to create the new driver repository.

    .. code-block:: bash

        cookiecutter https://github.com/Chemios/cookiecutter-chemios
        cookiecutter cookiecutter-chemios

3. Once you've created the repository, change into the directory and initialize git:

    .. code-block:: bash

        git init
        git add -A
        git commit -am "Initial Commit"

4. Then create a new repository on github (without a license or readme) and copy the https link.  Run the following command at your command line:

    .. code-block:: bash

        git remote add origin <link_to_repository>
        git push -u origin master

Now your driver is ready to use and synced to github.

.. _`python 3.0 or above`: https://www.python.org/downloads/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

