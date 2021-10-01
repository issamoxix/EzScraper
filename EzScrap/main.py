import pandas as pd
import requests as req
from bs4 import BeautifulSoup as Bs
import datetime
import os 


class table_to_csv:
    def __init__(self,url,all=True,index=False,file_name=None):
        self.url = url
        self.all = all
        self.index = index
        self.file_name=file_name

    # alltables function call the Parse table function and handle params
    def allTables(self):
        res = req.get(self.url)
        soup = Bs(res.text,'html.parser')
        tables_elem = soup.find_all('table')
        if self.index:
            self.ParseTable(tables_elem[int(self.index)-1],self.file_name)
            return 1
        if self.all:
            for i in tables_elem:
                self.ParseTable(i,self.file_name)
            return 1
        
    #getting data from every row and saving it in array then pushing it to the csv Dataframe
    #and the first row is the header
    def ParseTable(self,tableOI,file_name):
        table_rows_elem = tableOI.find_all('tr')
        table_headers = []
        for i in table_rows_elem:
            if len(i.find_all('td')) == 0:
                for th in i.find_all('th'):
                    table_headers.append(th.get_text())
                continue
        df = pd.DataFrame(columns=table_headers,index=None)
        for i in table_rows_elem:
            data = {}
            if len(i.find_all('td')) != 0:
                for td_index in range(0,len(i.find_all('td'))-1):
                    td = i.find_all('td')[td_index]
                    data[table_headers[td_index]] = td.get_text().strip()
                df = df.append(data,ignore_index=True)
            continue
        if not file_name:
            file_name = f"{datetime.datetime.now()}table_data".replace('-','_').replace(':','_').strip()
        file_name = self.CheckFileExists(file_name)
        df.to_csv(f'{file_name}.csv')
        return 1
    #this function below check if the file exists so we dont get file exists error
    def CheckFileExists(self,file_name):
        if os.path.exists(path=file_name+".csv"):
            try:
                return self.CheckFileExists(file_name.split('_')[0]+"_"+str(int(file_name.split('_')[1])+1))
            except:
                return self.CheckFileExists(file_name+"_0")
        else:
            return file_name
