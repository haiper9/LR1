from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=14'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', id='pagecontent')
    description = ''
    for tag in soup.findAll('span'):
        tag.decompose()
    for data in block:
        if data.find('a'):
            description = data.text
    save_result_in_file(description.splitlines())

def save_result_in_file(persons):
        file = open("persons.txt", "w")
        for person in persons:
            if person != "":
                file.write(person + "\n")
        file.close()