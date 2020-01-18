# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

page_url = "https://www.amazon.in/Amazon-FireTVStick-Alexa-Voice-Remote-Streaming-Player/dp/B0791YHVMK/ref=sr_1_1?keywords=fire+stick&qid=1579328339&sr=8-1"
browser_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

product_page = requests.get(page_url, headers=browser_agent)

soup = BeautifulSoup(product_page.content, "html.parser")

print(soup.prettify())

page_title = soup.find(id="productTitle").get_text()

product_price = soup.find(id="priceblock_ourprice").get_text()[2:8]

product_price = product_price.replace(',','')
final_price = float(product_price)

if(final_price<2900):
    send_email()
    
import smtplib

def send_email():
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("sender_email_id", "password_id")
    message = "Firestick price has dropped to ₹2800"    
    s.sendmail("sender_email_id","reciver_email_id", message)
    s.quit()
print(page_title.strip())    
