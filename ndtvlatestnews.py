from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.ndtv.com/latest').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('latest_news.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headlines', 'Summary', 'Link', 'Date'])

for article in soup.find_all('div', class_='new_storylising_contentwrap'):
    try:
        Headline = article.find('div', class_='nstory_header').a.text
    except Exception as e:
        Headline = None
    print(Headline)

    try:
        Summary = article.find('div', class_='nstory_intro').text
    except Exception as e:
        Summary = None
    print(Summary)

    try:
        Link = article.find('div', class_='nstory_header').a.get('href')
    except Exception as e:
        Link = None
    print(Link)

    try:
        Date = article.find('div', class_='nstory_dateline').text.split('|')[1]
    except Execution as e:
        Date = None
    print(Date)

    csv_writer.writerow([Headline, Summary, Link, Date])

csv_file.close()