import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import os 


class TableToCsv:
    def __init__(self, url, index=None, all_tables=True, filename=None):
        self.url = url
        self.index = index
        self.all_tables = all_tables
        self.filename = filename

    def parse_table(self, table_elem, filename):
        # Find all rows in the table
        rows = table_elem.find_all('tr')

        # Extract the header row
        header_row = None
        for row in rows:
            if row.find('th') is not None:
                header_row = row
                break

        # Extract the table headers
        headers = []
        for th in header_row.find_all('th'):
            headers.append(th.get_text().strip())

        # Extract the table data
        data = []
        for row in rows:
            if row == header_row:
                continue

            row_data = {}
            for i, td in enumerate(row.find_all('td')):
                row_data[headers[i]] = td.get_text().strip()

            data.append(row_data)

        # Create a Pandas DataFrame from the data and write it to a CSV file
        df = pd.DataFrame(data)
        if not filename:
            filename = f"{datetime.datetime.now()}table_data".replace('-','_').replace(':','_').strip()
        filename = self.check_file_exists(filename)
        df.to_csv(f'{filename}.csv', index=False)

    def check_file_exists(self, filename):
        # Check if the file exists, and if it does, add a suffix to the filename to make it unique
        if os.path.exists(f"{filename}.csv"):
            parts = filename.rsplit('_', 1)
            if len(parts) == 1:
                parts.append('0')
            else:
                try:
                    parts[1] = str(int(parts[1]) + 1)
                except ValueError:
                    parts[1] = '0'

            new_filename = '_'.join(parts)
            return self.check_file_exists(new_filename)

        return filename

    def extract_tables(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        tables = soup.find_all('table')
        if self.index is not None:
            self.parse_table(tables[int(self.index)], self.filename)
        elif self.all_tables:
            for table in tables:
                self.parse_table(table, self.filename)