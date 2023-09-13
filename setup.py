# Fix for older setuptools
# import re
# import os
# import sys

from setuptools import setup, find_packages


setup(
    name='My-Blueprint-Test',
    version='1.0.0',
    url='https://github.com/kuldeep3/my_blueprint_test',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    package_data={'spam': ['robot.txt']},
    py_modules=['bacon']
)
