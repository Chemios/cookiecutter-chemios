:tocdepth: 3

Introduction
============

Benefits
--------
-   **faster developement**: All the files and boilerplate for a new instrument driver can be created with one command.
-   **it's free**: This code is free and open source, so you can easily create and share drivers you write (unlike LabView)
-   **standardization**: Each instrument driver has a standard interface for all brands, making it easy to switch
    between brands without rewriting code (e.g, switch betwen Harvard Apparatus and New Era syringe pumps).
-   **cross platform**: The code is written in Python which is compatible with devices running Mac OS,
    Windows or Linux (including the Raspberry Pi).
-   **command line interface**: Each driver includes a command line interface for quickly testing a
    connection to an instrument or logging data to a file.
-   **maintanibility**: Best practices for driver development such as unit testing, continuous integration
    and autodocumentation are included.
-   **packaging**: Every driver can be published to PyPi_ and installed with a single :code:`pip install` command.

.. _PyPi: https://pypi.org/

Structure
----------

Each instance of a chemios instrument driver has a standard structure.
Here are some of the most important files in the temperature controllers driver as an example:

.. code-block:: bash

    chemios_tc/ #the folder for the chemios_tc package
        __init__.py
        chemios_tc_base.py #Contains template class for temperature controllers
        Omega9300Series.py #One type of a temperature controller
        cli.py #Source code for the commnad line interface
        utils.py #Useful Utilities
    docs/ #Contains file for building documentation
    tests/ #Unit tests of the driver
    new_instrument.py #Create the boilerplate for a new temperature controller
    requirements_dev.txt #Dependencies needed for development
    setup.py #Instructions for pacakaging the chemios_tc package

Some key benefits of this structure:

-   Once you run :code:`python setup.py`, your instrument driver can be imported
    into a python file.  For example with temperature controllers::code:`from chemios_tc import Omega9300Series`
-   Running :code:`new_instrument.py INSTRUMENT_NAME` will
    create a new file inside the package based on the template in base.py.
    It will also add the new class in that file to the package level (via __init__.py).

