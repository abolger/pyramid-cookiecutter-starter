============================
pyramid-cookiecutter-starter-AWS
============================

A Cookiecutter (project template) for creating a Pyramid starter project that can be deployed to Amazon Web Services Elastic Beanstalk (http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) . Project uses URL dispatch for routing and Jinja2 for templating. 

Requirements
------------
* Amazon Web Services free-tier account. 
* Python 2.7 or 3.4 (Amazon webservices supports these 2 python versions.)
* `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_

Usage
-----

1. Generate a Pyramid project, following the prompts from the command.

.. code-block:: bash

    $ cookiecutter https://github.com/abolger/pyramid-cookiecutter-starter-AWS

2. Finish configuring the project by creating a virtual environment and installing your new project. These steps are output as part of the cookiecutter command above and are slightly different for Windows.

.. code-block:: bash

    # Change directory into your newly created project.
    $ cd myproj
    # Create a virtual environment...
    $ python3 -m venv env
    # ...where we upgrade packaging tools...
    $ env/bin/pip install --upgrade pip setuptools
    # ...and into which we install our project and its testing requirements.
    $ env/bin/pip install -e ".[testing]"

3. Run your project's tests.

.. code-block:: bash

    $ env/bin/pytest

4. Run your project locally.

.. code-block:: bash

    $ env/bin/pserve development.ini

5. Install Elastic Beanstalk CLI (http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-getting-set-up.html).  

.. code-block:: bash  

    $ env/bin/pip install awsebcli


6. Deploy it to Amazon Elastic Beanstalk using the AWS eb Command line interface:

.. code-block:: bash
    $ 
