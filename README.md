# EzScraper

This is a Python package that converts HTML tables to CSV files. It provides a simple and efficient way to extract data from tables and store it in CSV format.


## Installation

You can install the package using pip:

```
pip install EzScraper
```

## Usage

The package provides a table_to_csv class that you can use to extract tables from HTML pages and convert them to CSV files. Here's an example:


```python
from EzScraper import table_to_csv

url = "https://www.worldometers.info/coronavirus/"
crawle = table_to_csv(url=url, file_name="my_table")
crawle.extract_tables()
```

This will extract all tables from the specified URL and save each one as a separate CSV file in the current working directory. You can also specify the index of the table you want to extract using the index parameter:
```python
table_to_csv(url, all=False, index=2, file_name='my_table')
```
This will extract the third table from the specified URL and save it as a CSV file with the name "my_table.csv" in the current working directory.


You can also use the file_name parameter to specify the name of the CSV file. If you don't specify a name, the package will generate a unique name based on the current date and time.

```python 
table_to_csv(url, all=True, index=False, file_name='my_data')
```

This will extract all tables from the specified URL and save them as CSV files with names like "my_data.csv", "my_data_1.csv", "my_data_2.csv", etc.

## Contributing

If you want to contribute to the package, please fork the repository, make your changes, and submit a pull request. Please include tests for any new features or bug fixes you add.
