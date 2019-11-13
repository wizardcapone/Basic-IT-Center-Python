from flask import Flask
from flask import request
import json

app = Flask(__name__)

products_all = []
@app.route("/")
def main_page():
	return "Our products are the best in Armenia, we deliver high-quality and reliable products in good packaging"
@app.route("/product", methods=["GET","POST"])
def products():
	global products_all
	if request.method == 'GET':
		return str(products_all)
	else:
		try: 
			myjson = request.get_json(force=False)
			return add_lists(myjson)
		except:
			return 'An error has occurred! CODE:[10]'
def add_lists(myjson):
	global products_all
	if myjson.get('type') != None and myjson.get('price') != None and myjson.get('name') != None:
		for data in products_all:
			if data['type'] == myjson['type'] and data['name'] == myjson['name']:
				return 'An error has occurred! CODE:[11]' 
		mydict = {}
		mydict['type'] = myjson['type']
		mydict['price'] = myjson['price']
		mydict['name'] = myjson['name']
		products_all.append(mydict)
		return str(products_all)
	else:
		return 'An error has occurred! CODE:[12]'
if __name__ == '__main__':
	app.run()