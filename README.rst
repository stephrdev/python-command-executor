command-executor
================

.. image:: https://img.shields.io/pypi/v/command-executor.svg
   :target: https://pypi.org/project/command-executor/
   :alt: Latest Version

.. image:: https://github.com/stephrdev/python-command-executor/workflows/Test/badge.svg?branch=master
   :target: https://github.com/stephrdev/python-command-executor/actions?workflow=Test
   :alt: CI Status

.. image:: https://codecov.io/gh/stephrdev/python-command-executor/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/stephrdev/python-command-executor
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/python-command-executor/badge/?version=latest
   :target: https://python-command-executor.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status


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

A Python 3 interpreter is required in addition to poetry.

.. code-block:: shell

    $ poetry install


Now you're ready to run the tests:

.. code-block:: shell

    $ make tests
