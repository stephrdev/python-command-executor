command-executor
================

.. image:: https://img.shields.io/pypi/v/command-executor.svg
   :target: https://pypi.python.org/pypi/command-executor
   :alt: Latest Version

.. image:: https://codecov.io/gh/moccu/python-command-executor/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/moccu/python-command-executor
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/python-command-executor/badge/?version=latest
   :target: https://python-command-executor.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/moccu/python-command-executor.svg?branch=master
   :target: https://travis-ci.org/moccu/python-command-executor

Usage
-----

Please refer to the `Documentation <https://python-command-executor.readthedocs.io/>`_ to
learn how to use ``command-executor``. Basicly, ``command_executor`` provides some
Python classes to make it easier to start processes / commands and handling errors and output.
In addition, input validation for command parameters is possible.


Requirements
------------

python-command-executor supports Python 3 only. No other dependencies are required.


Prepare for development
-----------------------

A Python 3.6 interpreter is required in addition to pipenv.

.. code-block:: shell

    $ pipenv install --python 3.6
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:

.. code-block:: shell

    $ pipenv run py.test
