import time
from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect('Alta.sqlite')
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Data

(id INTEGER PRIMARY KEY AUTOINCREMENT,
Product_Name VARCHAR(50),
Price VARCHAR(50));''')

i = 1
while True:
    url = 'https://alta.ge/smartphones-page-{}.html'.format(i)
    request = requests.get(url)
    time.sleep(15)
    status_code = request.status_code
    i += 1
    if i == 7: break
    if status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        div0 = (soup.find("div", {'class': 'ty-tygh'}))
        div1 = (div0.find("div", {'id': 'tygh_main_container'}))
        div2 = (div1.find("div", {'class': 'tygh-content clearfix'}))
        div3 = (div2.find("div", {'class': 'container-fluid category-grid inner-cg'}))
        div4 = (div3.find("div", {'class': 'row-fluid'}))
        div5 = (div4.find("div", {'class': 'span12'}))
        div6 = (div5.find("div", {'class': 'ty-mainbox-container clearfix'}))
        div7 = (div6.find("div"))
        div8 = (div7.find("div"))
        div9 = (div8.find("div"))
        div10 = (div9.find("div", {'class': 'grid-list'}))
        for each in div10.find_all("div", {'class': 'ty-column3'}):
            div11 = each.find("div", {'class': 'ty-grid-list__item ty-quick-view-button__wrapper'})
            div12 = div11.find("form")
            product_name0 = div12.find("div", {'class': 'ty-grid-list__item-name'})
            product_name = product_name0.find("a").text
            price1 = div12.find("div", {'class': 'ty-grid-list__price'})
            price2 = price1.find("span")
            price = price2.find("span").text

            cursor.execute("INSERT INTO Data(Product_Name, Price) VALUES (?,?)", (product_name, price))
            con.commit()
    else:
        print("cant connect to the server")

