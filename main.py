from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def jumush_izdoo():
    jobs = requests.get('https://devkg.com/ru/jobs').text
    soup = BeautifulSoup(jobs, 'lxml')
    vacancyes = soup.find_all('article', class_='item')
    dictary = {"company_name": [], "position": [], "price": [], "type_work": []}
    for vacancy in vacancyes:
        company_name = vacancy.find('div', class_='jobs-item-field company').text[8:].replace(' ', '')
        dictary["company_name"].append(company_name)
        position = vacancy.find('div', class_='jobs-item-field position').text[9:].replace(' ', '')
        dictary["position"].append(position)
        price = vacancy.find('div', class_='jobs-item-field price').text[9:]
        dictary["price"].append(price)
        type_work = vacancy.find('div', class_='jobs-item-field type').text[9:]
        dictary["type_work"].append(type_work)

    df = pd.DataFrame(dictary)
    df.to_csv("dbs.csv", index=False)


if __name__ == '__main__':
    while True:
        jumush_izdoo()
        time_wait = 5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
        print(jumush_izdoo())


