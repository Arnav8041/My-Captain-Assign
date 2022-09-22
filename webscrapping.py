import requests
from bs4 import BeautifulSoup

flipkart_url='https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_8_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_OUJ0NDXWZCCJ_wp2&fm=neo%2Fmerchandising&iid=M_d6ce1ced-1877-4f0c-9fac-b3f71947bc9e_3.OUJ0NDXWZCCJ&ppt=clp&ppn=mobile-phones-store&ssid=a8jdchhkls0000001663486660782'

req=requests.get(flipkart_url)
con=req.content

soup=BeautifulSoup(con,'html.parser')

all_phones=soup.find_all('div',{'class':'_2kHMtA'})

for phones in all_phones:
    phone_price=phones.find('div',{'class':'_30jeq3 _1_WHN1'}).text
    print(phone_price)