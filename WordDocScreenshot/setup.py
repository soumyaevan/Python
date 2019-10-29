import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'version.py'), encoding="utf-8") as f:
    VERSION = re.search("__version__ = '(.*)'", f.read()).group(1)

setup(
    name='rbfWordDocScreenShot',
    version=VERSION,
    description="Robot Framework test library for storing screenshot in Word document",
    author="Soumya Sen",
    author_email='sensoumya94@gmail.com',
    url='https://github.com/soumyaevan/rbfWordDocScreenshot.git',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation',
    platforms        = 'any',
    install_requires = ['python-docx','robotframework','shutil','os'],  
    classifiers=CLASSIFIERS,
    packages=['rbfWordDocScreenShot']
)