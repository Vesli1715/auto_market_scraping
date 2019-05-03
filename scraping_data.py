from bs4 import BeautifulSoup
import requests 


def parsing_data(brand, model, quantity):
	'''Get data from website, and return list of results[car, year, price]'''

	def quantity_of_cars(quantity):
		'''create correct value of quantity searching cars'''
		
		quantity = int(quantity/10) # depends from quantity position on page
		if quantity < 1:
			quantity = 1
		return quantity


	result = []	
	for i in range(quantity_of_cars(quantity)):
		r = requests.get(f'https://auto.ria.com/legkovie/{brand}/{model}/?page={i}')
		soup = BeautifulSoup(r.text, 'html.parser')  
		con = soup.find_all('div', attrs={'class':'content'})
		errors = 0

		for res in con:
			try:
				r = res.contents[1]
				car = r.find().text.strip()[:-5]
				year =  r.find().text.strip()[-4:]
				price = res.find('span', attrs={'class':'bold green size22'}).text
				result.append((car, year,  price))	
			except: 
				errors+=1
	return result

result = parsing_data('renault', 'megane', 10)
