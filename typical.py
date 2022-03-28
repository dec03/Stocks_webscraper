#create csv file

#contains company, ticker, weight, day, date, time

#use csv reader library

#use url: https://www.earningswhispers.com/stocks/ + ticker
#to get company info
#use a for loop for this

#scraping for loop

import csv
import requests
from bs4 import BeautifulSoup

list = []
spreadsheet = []


file_read = open('ticks_name.csv', 'r')
reader = csv.reader(file_read)

for row in reader:
    temp = row
    list.append(temp)
    spreadsheet.append(temp)

for i in list:
    print(i)

file_read.close()






file_write = open('updated_file.csv', 'w')
reader = csv.reader(file_write)
writer = csv.writer(file_write)
pos = 0
writer.writerow(['#', 'Company', 'Ticker', 'Weight', 'Day', 'Date', 'Time'])

for i in list:
    if i[0] != '#':
        pos += 1
        if list[pos][2] != 'MXIM':
            ticker = str(i[2])
            base_url = 'https://www.earningswhispers.com/stocks/'
            url = base_url+ticker
            print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.content, features="html.parser")
            results = soup.find(id='maindata')
            content = results.find_all(class_='boxhead')
            datebox = results.find_all(class_='mainitem')


            day = content[1]
            day = str(day.get_text())
            spreadsheet[pos][4] = day

            date = datebox[1]
            date = str(date.get_text())
            spreadsheet[pos][5] = date

            time = results.find(id='earningstime')
            time = str(time.get_text())
            spreadsheet[pos][6] = time

            writer.writerow(spreadsheet[pos])
            print(spreadsheet[pos])
        else:
            continue
file_write.close()
