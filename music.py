import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url='https://www.billboard.com/charts/hot-100'
data = requests.session().get(url, headers=headers)
def getrank():
    url='https://www.billboard.com/charts/hot-100'
    data=requests.session().get(url)
    soup=BeautifulSoup(data.content, 'html.parser')

    music=soup.select_one('span.chart-element__information')
    title = music.select_one('span.chart-element__information__song')
    music_title=title.text.strip()
    artist = music.select_one('span.chart-element__information__artist')
    tweet='1 . '+music_title+artist.text
    return tweet
