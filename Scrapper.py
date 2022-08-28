from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd



bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
soup = bs(page.text,'html.parser')

star_table = soup.find('table')
info = star_table.find("tbody")
table_rows = info.find_all('tr')

temp_list= []

for i, tr in enumerate(table_rows):
    print(i)
    tds = tr.find_all('td')
    for index,td in enumerate(tds):
        if index == 1:
            a = td.find("a")
            if a:
                temp_list.append(td.find("a").contents[0].replace("\n", ""))
            else:
                temp_list.append(td.contents[0].replace("\n", ""))
        elif index == 3:
            if len(td.contents) > 1:
                temp_list.append(td.contents[1].replace("\n", ""))
            else:
                temp_list.append(td.contents[0].replace("\n", ""))
        elif index == 6:
            temp_list.append(td.contents[0].replace("\n", ""))
        elif index == 7:
            temp_list.append(td.contents[0].replace("\n", ""))
        elif index == 8:
            temp_list.append(td.contents[0].replace("\n", ""))

print(temp_list)

header = ["proper_name", "distance", "mass", "radius", "luminosity"]
star_data = []

temp_star_data = []

for d in temp_list:
    temp_star_data.append(d)
    if len(temp_star_data) > 4:
        star_data.append(temp_star_data)
        temp_star_data = []

print(star_data)

df2 = pd.DataFrame(star_data, columns=header)
df2.to_csv("star_data.csv")