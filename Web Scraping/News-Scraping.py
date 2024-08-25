import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#loading html code from URL
page = urllib.request.urlopen('https://docs.python.org/3/library/random.html')
soup = bs(page, features="html.parser")

#finding all function names
names = soup.body.findAll('dt')
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

#finding all function description
description = soup.body.findAll('dd')
function_usage = []

for item in description:
    item = item.text
    item = item.replace('\n', ' ')
    function_usage.append(item)

#creating dataframe
data = pd.DataFrame({'function name': function_names, 'function usage': function_usage})

#targeting specific attributes
example = soup.body.findAll('section', attrs={'id': 'bookkeeping-functions'})

#storing dataframe to CSV file
data.to_csv('randon functions.csv')
