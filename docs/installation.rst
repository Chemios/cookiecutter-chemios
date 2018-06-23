
Installation (5 minutes)
=========================
Estimated Time: 5 minutes (if you already have python installed).

Step 1: Install Prerequesites
-----------------------------

You will need python 3.0 or above for this tutorial.
We suggest installing python via conda_, so you can use the
conda package manager.

First, you need to create and activate a virtual environment, which
will ensure a consistent development environment. Here is how to do it with
conda, but you can also use virtualenv_.

   .. code-block:: bash

        conda create -n YOUR_ENVIRONMENT_NAME
        source activate YOUR_ENVIRONMENT_NAME

Then, install cookiecutter_, which is a python library for creating projects from templates.

    .. code-block:: bash

        pip install -U cookiecutter

.. _conda: https://conda.io
.. _virtualenv: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html#step-1-install-cookiecutter
.. _cookiecutter: https://github.com/audreyr/cookiecutter

Step 2: Create a driver repository
------------------------------------

To create a new chemios driver repository, run the following command.
You will be prompted at the command line for the information needed to create the new driver repository.
See this :ref:`prompts` for a description of the prompts.

    .. code-block:: bash

        cookiecutter https://github.com/Chemios/cookiecutter-chemios

Step 3: Install Dev Requirements
--------------------------------

Change into the new directory for the instrument driver and run the following command.
Make sure your virtual environment is still activated
(you should see the name of the environemnt at your command prompt)

.. code-block:: bash

    pip install -r requirements_dev.txt

Next, we'll take a look at the struture of your new chemios driver.
