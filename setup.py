from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.2'
DESCRIPTION = 'Scraping HTML Tables from websites to csv file'
LONG_DESCRIPTION = 'This is a Python package that converts HTML tables to CSV files. It provides a simple and efficient way to extract data from tables and store it in CSV format.'

# Setting up
setup(
    name="EzScraper",
    version=VERSION,
    author="Issam Haidaoui (issamoxix)",
    author_email="<issamhaidaoui@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'beautifulsoup4', 'requests'],
    keywords=['python', 'Scraping', 'csv', 'Scraping Data', 'to csv file'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)