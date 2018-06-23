.. _prompts:

Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

developer_name
    Your full name.

email
    Your email address.

github_username
    Your GitHub username.

instrument_type
    The name your new instrument type. The plural form is preferred here (e.g., temperature controllers, pumps, etc.).

project_name (filled automatically)
    The name of your new instrument driver. This is used in documentation, so spaces and any characters are fine here.

project_slug (filled automatically)
    The namespace of your in. This should be Python import-friendly. Typically, it is the slugified version of project_name.

project_short_description (filled automatically)
    A 1-sentence description of what your drie does.

pypi_username
    Your Python Package Index account username.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

use_pytest
    If yes, this will set up a pytest runner for completing test

use_pypi_deployment_with_travis
    Whether to use PyPI deployment with Travis CI.
    This allows you to automatically package your driver, so it can be installed via pip.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', "No command-line interface"]

open_source_license
    Choose MIT here.
