Getting Started
===============

base.py as a template
---------------------
The heart of each chemios driver is a base.py file.
This file contains an `abstract base class`_ that models the interface for all instruments of that type.

For example, the temperature controllers base file has a set_temperature and get_current_temperature method:
Each temperature controller must implement the set_temperature and get_current_temperature methods.

.. code-block:: python

    # -*- coding: utf-8 -*-

    """Base Class for Temperature Controllers"""

    from abc import ABC

    class TemperatureControllers(ABC):
        '''Base Class for Temperature Controllers
        '''
        def get_current_temperature(self):
            ''' Method to get the current temperature
            Returns:
                update: dict

                update = {
                        'temp_set_point': setpoint in °C,
                        'current_temp': temperature in °C
                        }
            '''

        def set_temperature(self, temp_set_point):
            ''' Method to set the temperature
            Args:
                temp_set_point (float): temperature setpoint in °C
            Returns:
                update: dict

                update = {
                        'temp_set_point': setpoint in °C,
                        'current_temp': temperature in °C
                        }
            '''

The standard inteface is enforced by each temperature controller inheriting the TemperatureControllers base class.
See `Omega9300Series.py`_ for an example.

.. _`Omega9300Series.py`: https://github.com/Chemios/chemios-temperature_controllers/blob/master/chemios_tc/_omega9300series.py
.. _`abstract base class`: https://www.python-course.eu/python3_abstract_classes.php

New Instrument
--------------

To create a new instrument, we will use the :any:`../new_instrument.py` script.

This script creates a new instrument file based on the base file.
It also imports the newly created class inside that file to the package level (via __init__.py)
