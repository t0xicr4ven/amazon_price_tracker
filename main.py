import requests
from bs4 import BeautifulSoup 
import lxml

WEB_ADDRESS = "https://www.amazon.com.au/Samsung-Inch-Monitor-S27F350FHE-LS27R350FHEXXY/dp/B085D9DTJN/ref=sr_1_20?crid=18GRSO18K97ZL&dchild=1&keywords=widescreen+computer+monitor&qid=1629783463&sprefix=widescreen+%2Caps%2C342&sr=8-20"
IPAD_ADDRESS = "https://www.amazon.com.au/Apple-12-9-inch-iPad-Pro-Wi-Fi-256GB/dp/B093R19M8X/ref=sr_1_5?crid=2E1MDCDLO1YBB&dchild=1&keywords=ipad+pro+12.9&qid=1629786015&sprefix=ipad+%2Caps%2C347&sr=8-5"
HEADER = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
response = requests.get(url=IPAD_ADDRESS, headers=HEADER)
soup = BeautifulSoup(response.text, 'lxml')
# get price of item and remove the $ 
price_string = soup.find('span',
        id='priceblock_ourprice').getText().strip('$')
# remove , if string has one
new_string = price_string.replace(',','') 
print(int(float(new_string)))
