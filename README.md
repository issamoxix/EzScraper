# EzScraper

EzScraper allows to Scrape  table data from websites and save them as csv file


# Setup

```
pip install EzScraper
```

## How to use
```python
from EzScraper import table_to_csv
#using corona virus website as example
#in this example we will get all the tables
url = "https://www.worldometers.info/coronavirus/"
file_name = "CoronaData"
crawle = table_to_csv(url=url,file_name=file_name)
crawle.allTable()

#CoronaData.csv files will be created in the same directory
```
