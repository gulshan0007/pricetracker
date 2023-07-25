from bs4 import BeautifulSoup
import requests
import smtplib
import time

URL = 'https://www.amazon.in/gp/product/B093LK1BBT/ref=ox_sc_saved_title_5?smid=AXOGFIT0PZZ7G&psc=1'

headers={
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(class_="a-price-whole").get_text()
    converted_price=int(price.replace(',', ''))



    if(converted_price < 6000):
        send_mail()

    print(converted_price)
    print(title.strip())


    if(converted_price < 6000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gulshankumar060102@gmail.com','ipdtnbuygnamcjhe')
    subject='Price fell down'
    body='Check the amazon link https://www.amazon.in/gp/product/B093LK1BBT/ref=ox_sc_saved_title_5?smid=AXOGFIT0PZZ7G&psc=1'

    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'gulshankumar060102@gmail.com',
        'gulshankrsah2002@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
