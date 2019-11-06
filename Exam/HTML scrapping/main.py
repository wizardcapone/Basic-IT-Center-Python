from bs4 import BeautifulSoup as soup
import requests, pymysql, re

class ConnectDB():
	def __init__(self, host, user, passh, db):
		self.__host = host
		self.__user = user
		self.__passh = passh
		self.__db = db
	def connect(self):
		connection = pymysql.connect(host=self.__host,
                             user=self.__user,
                             password=self.__passh,                             
                             db=self.__db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		return connection
class ReuqestDB():
	def __init__(self, conn, table, keys, values):
		self.__conn = conn
		self.__table = table
		self.__keys = keys
		self.__values = values
	def insert(self):
		sql = """INSERT INTO `%s` (%s) VALUES (%s)""" % (self.__table,self.__keys,self.__values)
		return self.__conn.execute(sql)
def scrapping(url):
	global soup

	products = {}

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	try: 
		base_url = requests.get(url, headers=headers).text

		soup = soup(base_url, 'lxml')

		products['title'] = soup.find('h1', {"id": "grpDescrip_h"}).span.text.strip()
		# pattern = '[0-9]+\.[0-9]+'
		# products['price'] = re.findall(pattern, products['price'])[0]
		products['rating'] = soup.find('div', class_="grpRating").a.text.split()[0]
		products['description'] = ''
		for row in soup.find_all('li', class_="item"):
			products['description'] += row.text.strip() + '\n'
		return products
	except:
		print('Error: Invalid URL or lost connection')
	return False
def main():
	c = ConnectDB('localhost','root','','scrapping')
	conn = c.connect()

	if not conn:
		print('Connection to the database failed.')

	connection = conn.cursor()

	url = input('Input Product URL: ')

	print('Trying to scrap data from: https://www.newegg.com/p/'+url+'..')

	products = scrapping('https://www.newegg.com/p/'+url+'')

	if not products:
		print('Unsuccess scrap!')
		return

	insert_values = str("'") + str(products['title']) + str("'") + str(",") + str("'") + str(products['rating']) + str("'") + str(",") + str("'") + str(products['description']) + str("'") + str(",") + str("'") + str(url) + str("'")
	request = ReuqestDB(connection, 'products','title,rating,description,product_url',insert_values)
	request.insert()
	conn.commit()
	conn.close()
	print('scraping data successfully sent to DB.')
if __name__ == '__main__':
	main()


