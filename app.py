import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.koreaboardgames.com/boardgame/game_list01.php#pagenum',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#gameList > li:nth-child(1)')

for tr in trs:
    title = tr.select_one('div.desc > p > a').text
    psn = tr.select_one('table > tbody > tr:nth-child(2) > td').text
    age = tr.select_one('table > tbody > tr:nth-child(3) > td').text
    time = tr.select_one('table > tbody > tr:nth-child(4) > td').text
    print(title)