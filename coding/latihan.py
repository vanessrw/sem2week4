import bs4
import requests

url = requests.get('https://www.newegg.com/p/pl?d=laptop')
soup = bs4.BeautifulSoup(url.text, 'html.parser')

containers = soup.select('.item-container')

for container in containers:
	brands = container.select('.item-branding');
	brand = brands[0].img['title'].strip()
	
	prices = container.select('.price-current');
	price = prices[0].text.strip()

 print("Brand: " + brand)
 print("Product: " + product)
 print("Price: " + price)
