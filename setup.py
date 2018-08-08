import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('command_executor').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='command-executor',
    version=VERSION,
    description=(
        'command_executor provides some Python classes to make it easier to '
        'execute processes / commands and handling errors and output.'
    ),
    long_description=long_description,
    url='https://github.com/moccu/python-command-executor',
    project_urls={
        'Bug Reports': 'https://github.com/moccu/python-command-executor/issues',
        'Source': 'https://github.com/moccu/python-command-executor',
    },
    author='Moccu GmbH & Co. KG',
    author_email='info@moccu.com',
    packages=find_packages(exclude=['docs', 'tests', 'tests.*']),
    install_requires=[],
    include_package_data=True,
    keywords='commands shell processes',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
