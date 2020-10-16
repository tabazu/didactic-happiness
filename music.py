import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url='https://www.melon.com/chart/index.htm'
data = requests.session().get(url, headers=headers)
def getrank():
    url='https://www.melon.com/chart/index.htm'
    data=requests.session().get(url, headers=headers)
    soup=BeautifulSoup(data.content, 'html.parser')
    music=soup.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div')
    title = music.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a')
    music_title=title.text.strip()
    artist = music.select_one('#frm > div > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > div.ellipsis.rank02 > a')
    tweet='1 . '+music_title+' '+artist.text
    return tweet
