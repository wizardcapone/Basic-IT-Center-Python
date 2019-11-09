from datetime import datetime
import pymysql, time

class ConnectDB():
	def __init__(self, host, user, password, db):
		self.__host = host
		self.__user = user
		self.__password = password
		self.__db = db
	def connect(self):
		self.__connection = pymysql.connect(host=self.__host,
                             user=self.__user,
                             password=self.__password,                             
                             db=self.__db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
		return self.__connection
class RequestDB():
	def __init__(self, conn, table, where=False, arg=False, arg2=False, limit=False, order=False):
		self.__conn = conn
		self.__table = table
		self.__where = where
		self.__arg = arg
		self.__arg2 = arg2
		self.__limit = limit
		self.__order = order
		self.__cur = self.__conn.cursor()
	def select(self):
		if self.__where != False and self.__arg != False:
			if self.__limit == False:
				if self.__order == False:
					sql_select = """SELECT * FROM %s WHERE `%s` = %s""" % (self.__table,self.__where,self.__arg)
					self.__cur.execute(sql_select)
				else:
					sql_select = """SELECT * FROM %s WHERE `%s` = %s ORDER BY `date_it` %s""" % (self.__table,self.__where,
						self.__arg,
						self.__order)
					self.__cur.execute(sql_select)
			else:
				if self.__order == False:
					sql_select = """SELECT * FROM %s WHERE `%s` = %s LIMIT %d""" % (self.__table,self.__where,self.__arg,self.__limit)
					self.__cur.execute(sql_select)
				else:
					sql_select = """SELECT * FROM %s WHERE `%s` = %s ORDER BY `date_it` %s LIMIT %d""" % (self.__table,self.__where,
						self.__arg,
						self.__limit,
						self.__order)
					self.__cur.execute(sql_select)
		else:
			sql_select = """SELECT * FROM %s""" % (self.__table)
			self.__cur.execute(sql_select)
		return self.__cur
	def insert(self):
		sql_insert = """INSERT INTO %s (%s) VALUES (%s)""" % (self.__table,self.__where,self.__arg)
		self.__cur.execute(sql_insert)
		return self.__cur
	def update(self):
		sql_update = """UPDATE %s SET %s = %s WHERE %s = %s""" % (self.__table,self.__where,self.__arg,self.__arg2,self.__limit)
		self.__cur.execute(sql_update)
		return self.__cur
database = ConnectDB('localhost','sammy','botinbot2019','mybot')
conn = database.connect()
request = RequestDB(conn, 'contracts','status',1)
query = request.select()
if query.rowcount > 0:
	fetchl = query.fetchall()
	date_format = '%Y-%m-%d %H:%M:%S'
	for row in fetchl:
		contract_id = row['id']
		ts = time.time()
		d1 = datetime.fromtimestamp(ts)
		d2 = datetime.strptime(str(row['date_update']), date_format)
		diff = d1 - d2
		if diff.days > 0:
			di1 = datetime.fromtimestamp(ts)
			di2 = datetime.strptime(str(row['date_start']), date_format)
			diff2 = di1 - di2
			if row['type'] == 1:
				percent = 30
			elif row['type'] == 2:
				percent = 35
			elif row['type'] == 3:
				percent = 40
			result_working = round((row['cost'] / 100 * percent) / 7)
			user_id = row['user_id']
			request = RequestDB(conn, 'accounts','user_id',user_id,0,1)
			query = request.select()
			if query.rowcount > 0:
				fetchuser = query.fetchall()
				user_cash = fetchuser[0]['balance']
				working = row['working']
				user_cash += result_working
				working += result_working
				request = RequestDB(conn, 'accounts','balance',user_cash,'user_id',user_id)
				query = request.update()
				conn.commit()
				request = RequestDB(conn, 'contracts','working',working,'id',contract_id)
				query = request.update()
				conn.commit()
				if diff2.days >= 7:
					request = RequestDB(conn, 'contracts','status',2,'id',contract_id)
					query = request.update()
					conn.commit()
conn.close()