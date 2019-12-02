import requests
from bs4 import BeautifulSoup as bs

headers = {"accept": "image/webp,image/apng,image/*,*/*;q=0.8",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

base_url = "https://postila.ru/id"
user_id = 7163810

""" 
генерация ай ди страницы и вызывает вторую функцию

"""


def id_cycle(base_url, user_id):
    while user_id > 0:
        user_id = user_id - 1
        new_id = (base_url + str(user_id))
        print(new_id)
        Func(new_id)


""" 
  вторая функция выполняет подключения к страницы по айди.
  Затем начинает парсинг имейлов и записывает в txt
  

"""


def Func(new_id):
    session = requests.Session()
    request = session.get(new_id, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "lxml")
        divs = soup.find_all("div", {"class": "socialButtons"})
        f = open("parse_zero.txt", "a")
        try:
            for div in divs:
                href = div.find("a")["href"]
                f.write(href + "\n")
                print(href)
        except TypeError:
            print("Fish")
    else:
        print("Error")


id_cycle(base_url, user_id)
