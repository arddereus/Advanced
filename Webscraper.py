import webbrowser, sys, pyperclip, requests, bs4
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from datetime import datetime
import locale
import pandas as pd
import numpy as np

res = requests.get('http://www.fabpedigree.com/james/mathmen.htm')
res.raise_for_status()
MatM = bs4.BeautifulSoup(res.text, "html.parser")
MatM2 = []
for i, li in enumerate(MatM.select('li')):
     MatM2.append(li.text)
MatM3 = [i.split('\n', 1)[0] for i in MatM2]

dates = []
length = 30

def GetEdit(Name):
     locale.setlocale(locale.LC_TIME, "nl_NL")
     res2 = requests.get('https://nl.wikipedia.org/wiki/' + Name)
     res2.raise_for_status()
     html = bs4.BeautifulSoup(res2.text, "html.parser")

     laatste_bewerkt = html.find(id="footer-info-lastmod")
     datum = datetime.strptime(str(laatste_bewerkt)[72:-6], "%d %b %Y om %H:%M")
     return datum.isoformat()


for i in range(length):
     MatM4 = MatM3[0:length]
     try:
          dates.append(GetEdit(MatM3[i]))
     except:
          dates.append(None)

df = pd.DataFrame(list(zip(MatM4, dates)),
      columns =['Name', 'Date'])
df = df[df.Date.notnull()]
FinalFrame = df.sort_values(by=['Date'])
lastname = FinalFrame.iloc[0]['Name']
lasttime = FinalFrame.iloc[0]['Date']
print(FinalFrame)

print('The poor guy' + lastname + ' was edited last at ' + lasttime + '...')

answer = input("Do you wanna help the Scientific Community, by updating this webpage?")
if answer == 'yes':
     print("Okay, let's Go!")
     webbrowser.open('https://nl.wikipedia.org/w/index.php?title=' + lastname + '&action=edit')
else:
     webbrowser.open('https://www.google.com/search?q=why+mathematics+and+philosophy+is+important&oq=why+mathematics+and+philo&aqs=chrome.1.69i57j33l7.8487j0j4&sourceid=chrome&ie=UTF-8')








