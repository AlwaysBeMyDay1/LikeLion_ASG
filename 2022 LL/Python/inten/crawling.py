import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.naver.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

menus = soup.findAll("a","nav")
file = open("NaverMenu.txt","w",encoding="UTF-8")

dateInfo = datetime.today().strftime("%Y년 %m월 %d일의 네이버 메뉴입니다. \n")
file.write(dateInfo)
print(dateInfo)

for index, menu  in enumerate(menus) :
    doc = str(index+1) +"번 메뉴 : "+ menu.get_text() +"\n"
    file.write(doc)
    print(doc)


file = open("NaverMenu.txt","w",encoding="UTF-8")

for menu in menus:
	file.write(menu.get_text()+"\n")