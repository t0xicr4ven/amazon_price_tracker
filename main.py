import requests
from bs4 import BeautifulSoup 
import lxml
import smtplib
import os


"""You could put a bunch of items into a csv and loop through and check price
on each"""

EMAIL_ADD = os.environ.get('email_add')
EMAIL_PASS = os.environ.get('email_pass')

MAX_PRICE_TO_PAY = 1800
IPAD_ADDRESS = "https://www.amazon.com.au/Apple-12-9-inch-iPad-Pro-Wi-Fi-256GB/dp/B093R19M8X/ref=sr_1_5?crid=2E1MDCDLO1YBB&dchild=1&keywords=ipad+pro+12.9&qid=1629786015&sprefix=ipad+%2Caps%2C347&sr=8-5"

 HEADER = {
         'User-Agent': """SET YOUR USER AGENT. GOOGLE MY USER AGENT AND YOU'LL
         FIND IT""",
          'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
       }

response = requests.get(url=IPAD_ADDRESS, headers=HEADER)
soup = BeautifulSoup(response.text, 'lxml')

# get price of item and remove the $ 
price_string = soup.find('span',
        id='priceblock_ourprice').getText().strip('$')

# remove , if string has one
new_string = price_string.replace(',','') 

# check if price is below users set price
def check_if_cheap(current_price):
    if current_price < MAX_PRICE_TO_PAY:
        send_email()
    else:
        pass

# send email sayin price is below max price willing to pay and add the link
def send_email():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADD, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADD,to_addrs=EMAIL_ADD,msg=f"""Subject:
                Amazon Item\n\nThe it below  your price, go buy NOW --
                {IPAD_ADDRESS}""")
