Next Steps
==============

Create a GitHub Repo
---------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter. This is so that Travis CI and pyup.io can find it when we get to Step 5.

``If your virtualenv folder is within your project folder, be sure to add the virtualenv folder name to your .gitignore file.``

You will find one folder named after the ``[project_slug]``. Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:myusername/mypackage.git
    git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You'll need a ssh key to push the repo. You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

Set Up Travis CI
-----------------

`Travis CI org`_ [*]_ is a continuous integration tool used to prevent integration problems. Every commit to the master branch will trigger automated builds of the application.

Login using your Github credentials. It may take a few minutes for Travis CI to load up a list of all your GitHub repos. They will be listed with boxes to the left of the repo name, where the boxes have an ``X`` in them, meaning it is not connected to Travis CI.

Add the public repo to your Travis CI account by clicking the ``X`` to switch it "on" in the box next to the ``mypackage`` repo. Do not try to follow the other instructions, that will be taken care of next.

In your terminal, your virtualenv should still be activated. If it isn't, activate it now. Run the Travis CLI tool to do your Travis CI setup:

.. code-block:: bash

    travis encrypt --add deploy.password

This will:

* Encrypt your PyPI password in your Travis config.
* Activate automated deployment on PyPI when you push a new tag to master branch.

See :ref:`travis-pypi-setup` for more information.

.. [*] For private projects go to `Travis CI com`_

.. _`Travis CI org`: https://travis-ci.org/
.. _`Travis CI com`: https://travis-ci.com/


Set Up ReadTheDocs
--------------------------

`ReadTheDocs`_ hosts documentation for the open source community. Think of it as Continuous Documentation.

Log into your account at `ReadTheDocs`_ . If you don't have one, create one and log into it.

If you are not at your dashboard, choose the pull-down next to your username in the upper right, and select "My Projects". Choose the button to Import the repository and follow the directions.

In your GitHub repo, select Settings > Webhooks & Services, turn on the ReadTheDocs service hook.

Now your documentation will get rebuilt when you make documentation changes to your package.

.. _`ReadTheDocs`: https://readthedocs.org/

Set Up pyup.io
----------------------

`pyup.io`_ is a service that helps you to keep your requirements files up to date. It sends you automated
pull requests whenever there's a new release for one of your dependencies.

To use it, create a new account at `pyup.io`_ or log into your existing account.

Click on the green ``Add Repo`` button in the top left corner and select the repo you created in Step 3. A popup will
ask you whether you want to pin your dependencies. Click on ``Pin`` to add the repo.

Once your repo is set up correctly, the pyup.io badge will show your current update status.

.. _`pyup.io`: https://pyup.io/

Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

When you are ready, release your package the standard Python way.

See `PyPI Help`_ for more information about submitting a package.

Here's a release checklist you can use: https://gist.github.com/audreyr/5990987

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html
