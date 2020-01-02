import webbrowser, sys, pyperclip, requests, bs4
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

res = requests.get('http://www.fabpedigree.com/james/mathmen.htm')
res.raise_for_status()
MatM = bs4.BeautifulSoup(res.text, "html.parser")
MatM2 = []
for i, li in enumerate(MatM.select('li')):
     MatM2.append(li.text)
MatM3 = [i.split('\n', 1)[0] for i in MatM2]

dates = []
def GetEdit(Name):
     res2 = requests.get('https://nl.wikipedia.org/wiki/' + Name)
     res2.raise_for_status()

     html = bs4.BeautifulSoup(res2.text, "html.parser")
     for li in html.find_all('li'):
          print(li.find_all('footer-info-lastmod'))

Name2 = (MatM3[0])
print(GetEdit(Name2))

# hit_link = [li for li in html.select('li')
# if li['.id'].find('footer-info-lastmod') > -1]
# return hit_link
# html2 = html.select('ul li')
# <li id="footer-info-lastmod"> This page was last edited on 20 December 2019, at 02:27<span class="anonymous-show">&nbsp;(UTC)</span>.</li>




# name = MatM3[0]
# def obtainpop(name):
# res2 = requests.get('https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/' + name)
# pophtml = bs4.BeautifulSoup(res2.text, "html.parser")
# print(pophtml)

# print(obtainpop(name = MatM3[0]))




    # if response is not None:
    #     html = BeautifulSoup(response, 'html.parser')
    #     hit_link = [a for a in html.select('a')
    #                 if a['href'].find('latest-60') > -1]
    #
    #     if len(hit_link) > 0:
    #         # Strip commas
    #         link_text = hit_link[0].text.replace(',', '')
    #         try:
    #             # Convert to integer
    #             return int(link_text)
    #         except:
    #             log_error("couldn't parse {} as an `int`".format(link_text))
    #
    # log_error('No pageviews found for {}'.format(name))
    # return None






