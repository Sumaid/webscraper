import csv
from bs4 import BeautifulSoup
from requests import get

with open('in_book.csv', 'w') as myFile:
    writer = csv.writer(myFile, delimiter=";", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["NAME", "URL",  "Author", "Price",
                     "Number of Ratings", "Average Rating"])
    for page in range(1, 6):

        url = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_" + \
            str(page)+"?ie=UTF8&pg="+str(page)
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        book_containers = html_soup.find_all('div', class_='zg_itemImmersion')

        for book in book_containers:

            if len(book.find_all('a', class_='a-link-normal')) > 0:
                url = "https://www.amazon.in" + \
                    book.find_all('a', class_='a-link-normal')[0].get('href')
            else:
                url = "Not available"

            if len(book.find_all('div', class_='p13n-sc-truncate')) > 0:
                name = book.find_all('div', class_='p13n-sc-truncate')[0].text
            else:
                name = "Not available"

            if len(book.find_all('div', class_='a-size-small')) > 0:
                author = book.find_all('div', class_='a-size-small')[0].text
            else:
                author = "Not available"

            if len(book.find_all('span', class_='p13n-sc-price')) > 0:
                price = "₹" + \
                    book.find_all('span', class_='p13n-sc-price')[0].text
            else:
                price = "Not available"

            if len(book.find_all('a', class_='a-size-small a-link-normal')) \
               > 0:
                ratenumber = book.find_all(
                    'a', class_='a-size-small a-link-normal')[0].text
            else:
                ratenumber = "Not available"

            if len(book.find_all('span', class_='a-icon-alt')) > 0:
                stars = book.find_all('span', class_='a-icon-alt')[0].text
            else:
                stars = "Not available"

            writer.writerow([name, url,  author, price, ratenumber, stars])

