from requests import get
from bs4 import BeautifulSoup

def GetPage():
    from requests import get

    URL = input("url:")
    page = get(URL)

    print(page.text)


from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://lnu.edu.ua"
URL = BASE_URL + "/about/faculties/"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

site = get(URL, headers=HEADERS)
site = BeautifulSoup(site.content, "html.parser")

with open("data.txt", "w", encoding='utf-8') as f:
    # пошук елементів через for
    for faculty in site.find("ul", class_="structural-units").find_all("li"):
        # пошук елемента титулки h2 + додавання у файл
        txt = faculty.find("h2").text
        # пошук посилання і додавання його у файл
        href = faculty.find("div", class_="details").find_all("p")[-1].find("span", class_="value").find("a").text
        email = faculty.find("div", class_="details").find_all("p")[2].find("span", class_="value").find("a").text
        url = "https://" + href
        print(txt)
        print(url)
        print(email)
        f.writelines(txt + "\n")
        f.writelines(url + "\n")
        f.writelines(email + "\n")
