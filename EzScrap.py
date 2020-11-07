import requests as req 
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
class Es:
    def __init__(self,url):
        
        self.url = url
        if not self.url : return print('Enter A url !!')
        self.parse_table()
    def parse_table(self):
        self.res = req.get(self.url)
        
        if'<body>' in self.res.text:
            x = self.res.text.split('<body>')
            y = x[1].split('</body>')
            self.body = y[0]
        else: 
            self.body = self.res.text

        self.doc = BeautifulSoup(self.body,"html.parser")
        self.table_len = len(self.doc.find_all('table'))
    def pross(self):
        
        
        for r in range(self.table_len):
            self.table = self.doc.find_all('table')[r]
            
            self.rows = self.table.find_all('tr')
            self.col = []
            for i in self.rows:
                if i == self.rows[0]:
                    continue
                self.col.append(i.text.split())
            print(tabulate(self.col, headers=self.rows[0].text.split()))
            print('=============================================\n')
            ch = input('Table ('+str(r)+') | Press C to save as csv file | Press Enter to continue | Press Q To Quit : ')
            if ch.lower() == "q":
                break
            if ch.lower() == "c":
                self.table_to_csv(r)
        
    def table_to_csv(self,t_number):
        self.data = []
        self.parsed_data = []
        self.table = self.doc.find_all('table')[t_number]
        self.rows = len(self.table.find_all('tr'))
        for h in range(len(self.table.find_all('td'))):
                if self.table.find_all('td')[h].string == None:
                    print(h,'/',len(self.table.find_all('td')))
                    self.table.find_all('td')[h].string = "NaN"
        for r in range(self.rows):
            arr = self.table.find_all('tr')[r].text.split()
            print('(',r,'/',self.rows,')')
            # set the empty td to NaN 
             
            for f in range(len(arr)):
                if ',' in arr[f]:   
                    print('Replace',f,'/',len(arr))
                    # replace , to " " in numbers 
                    arr[f] = arr[f].replace(',','')
            
            self.parsed_data.append(arr)
            
        with open('data'+str(t_number)+'.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.parsed_data)
        print('Data Saved in data'+str(t_number)+'.csv file')
           