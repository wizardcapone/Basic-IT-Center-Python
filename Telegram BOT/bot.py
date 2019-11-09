# coding=utf8
# Автор Wizard Capone (Artyom Samsonyan) v1.0.2
from random import randint as rnd
from datetime import datetime
import telebot, pymysql, re, time, requests
from telebot import types

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
	def __init__(self, conn, table, where, arg, arg2=False, limit=False, order=False):
		self.__conn = conn
		self.__table = table
		self.__where = where
		self.__arg = arg
		self.__arg2 = arg2
		self.__limit = limit
		self.__order = order
		self.__cur = self.__conn.cursor()
	def select(self):
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
		return self.__cur
	def insert(self):
		sql_insert = """INSERT INTO %s (%s) VALUES (%s)""" % (self.__table,self.__where,self.__arg)
		self.__cur.execute(sql_insert)
		return self.__cur
	def update(self):
		sql_update = """UPDATE %s SET %s = %s WHERE %s = %s""" % (self.__table,self.__where,self.__arg,self.__arg2,self.__limit)
		self.__cur.execute(sql_update)
		return self.__cur
class users():
	def __init__(self, user_id):
		self.user_id = user_id
		self.position = 1
		self.clicked = 0
		self.withdraw = 0
		self.cost = 0
		self.current_page = 0
		self.delete_message = 0
		self.message_id = 0
		self.buy_contract = 0
		self.deposit_sum = 0
		self.open_deposit = 0
		self.sum_payment = ''
		self.contract_sum = 0
all_data = {}
types = telebot.types
bot = telebot.TeleBot('821583839:AAHtT-4dn5YfTlAxTLfSM9RsEigdzRErCvg', threaded=False)
def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None
@bot.message_handler(commands=['start'])
def send_welcome(message):
	global all_data
	unique_code = extract_unique_code(message.text)
	database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
	conn = database.connect()
	user_id = message.from_user.id
	request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
	query = request.select()
	if query.rowcount == 0:
		balance = 0
		arr_insert = str(message.from_user.id) + str(",") + str(balance)
		request = RequestDB(conn, 'accounts','user_id,balance',arr_insert)
		query = request.insert()
		conn.commit()
		if unique_code != None:
			referal_insert = str(unique_code) + str(",") + str(message.from_user.id) + str(",") + str(0)
			request = RequestDB(conn, 'referals','user_id,referal_id,earnings',referal_insert)
			query = request.insert()
			conn.commit()
	if all_data.get(message.from_user.id) == None:
		data = users(message.from_user.id)
		all_data[message.from_user.id] = data
	message_text = "''Добро пожаловать "+message.from_user.first_name+"''"
	bot.send_message(message.chat.id, message_text, reply_markup=keyboard(message.chat.id))
	conn.close()
@bot.message_handler(content_types=['text'])
def send_text(message):
	global all_data
	if all_data.get(message.from_user.id) != None:
		user = all_data[message.from_user.id]
		pattern = '^(🛒Мой аккаунт)'
		str_find = re.findall(pattern, message.text)
		if message.text == '🔄 Рестарт' and user.clicked == 0:
			user.clicked = 1
			bot.send_message(message.chat.id, 'Рестартируем приложение', reply_markup=keyboard(message.chat.id))
		elif message.text == '👤 Ваш аккаунт' or message.text == '👤 Аккаунт' and user.clicked == 0:
			user.clicked = 1
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=account(message.chat.id))
		elif message.text == '⚙ Настройки' and user.clicked == 0:
			user.clicked = 1
			user.position = 1
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=settings(message.chat.id))
		elif message.text == '❓ Почему мы?' and user.clicked == 0:
			user.clicked = 1
			decoded_string = "Хотите прибыли? Развития и возможность на будущее? Что же, вам определенно к нам. Поскольку юная группа, полная энергии и идей начала развития нового вида, по стандартам что ещё не оказались на нынешнем рынке. Зачем задумываться, если нужно просто попробовать и убедиться на личном опыте? Не теряйте шанса, жизнь это ритм, так двигайтесь вместе с нами вперёд.\n\nВаш нынешний день, можете изменить лишь вы, с помощью нас!"
			bot.send_message(message.chat.id, decoded_string, reply_markup=previous(message.chat.id))
		elif message.text == '📊 Развитие' and user.clicked == 0:
			user.clicked = 1
			bot.send_message(message.chat.id, 'Доброе времени суток!\n\nДорогие клиенты нашей платформы «EvocaBot»\n\nМы рады приветствовать вас на нашей платформе. Команда разработчиков работает без перерывов, для улучшение нашей платформы и обещает постоянно радовать вас обновлениями. Развивать нашу платформу в лучшую сторону. Надеемся на вашу поддержку. В данном разделе будут публиковаться новости о обновлениях.', reply_markup=previous(message.chat.id))
		elif message.text == '↩ Назад' and user.position == 1 and user.clicked == 0:
			user.clicked = 1
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=keyboard(message.chat.id))
			user.withdraw = 0
		elif message.text == '↩ Назад' and user.position == 2 and user.clicked == 0:
			user.clicked = 1
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=account(message.chat.id))
			user.withdraw = 0
			user.cost = 0
			user.position = 1
			user.open_deposit = 0
		elif message.text == '↩ Назад' and user.position == 3 and user.clicked == 0:
			user.clicked = 1
			user.buy_contract = 0
			user.position = 2
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=contracts(message.chat.id))
		elif message.text == '↩ Назад' and user.position == 4 and user.clicked == 0:
			user.clicked = 1
			user.position = 1
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=settings(message.chat.id))
		elif message.text == '↩ Назад' and user.position == 5 and user.clicked == 0:
			user.clicked = 1
			user.position = 2
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=referals(message.chat.id))
		elif user.withdraw == 1:
			if message.text.isdigit():
				user.cost = int(message.text)
				if user.cost > 0:
					database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
					conn = database.connect()
					request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
					query = request.select()
					fetchl = query.fetchall()
					if fetchl[0]['balance'] >= user.cost:
						bot.send_message(message.chat.id, 'Пожалуйста укажите ваш Payeer счёт для вывода средств', reply_markup=previous(message.chat.id))
						user.withdraw = 2
					else:
						bot.send_message(message.chat.id, 'На вашем счету недостаточно средств для вывода %d рублей' % user.cost, reply_markup=previous(message.chat.id))
					conn.close()
		elif user.withdraw == 2:
			regex_string = '^P([0-9]{10})$'
			find_regex = re.findall(regex_string, message.text)
			if len(find_regex) > 0:
				if len(message.text) == 11:
					payeer = str(message.text)
					database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
					conn = database.connect()
					request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
					query = request.select()
					if query.rowcount == 1:
						fetchl = query.fetchall()
						user_cash = fetchl[0]['balance']
						user_cash -= user.cost
						arr_insert = str(message.from_user.id) + str(",") + str(user.cost) + str(",") + str("'") + str(payeer) + str("'") + str(",") + str(0)
						request = RequestDB(conn, 'withdraw','user_id,cost,payeer,status',arr_insert)
						query = request.insert()
						conn.commit()
						user.withdraw = 0
						bot.send_message(message.chat.id, 'Вы успешно выставили счёт в размере %d рублей на свой Payeer кошелек %s !' % (user.cost, payeer), reply_markup=previous(message.chat.id))
						request = RequestDB(conn, 'accounts','balance',user_cash,'user_id',message.from_user.id)
						query = request.update()
						conn.commit()
					else:
						bot.send_message(message.chat.id, 'Ошибка!', reply_markup=previous(message.chat.id))
					conn.close()
				else:
					bot.send_message(message.chat.id, 'Ошибка! пожалуйста введите правильный Payeer кошелек', reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Ошибка! пожалуйста введите правильный Payeer кошелек', reply_markup=previous(message.chat.id))
		elif message.text == '📰 Контракты | Статус: Не активен' or message.text == '📰 Контракты | Статус: Активен ✅' and user.clicked == 0:
			user.clicked += 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
			query = request.select()
			fetchl = query.fetchall()
			request2 = RequestDB(conn, 'contracts','user_id',message.from_user.id)
			query2 = request2.select()
			if query2.rowcount != 0:
				fetchl2 = query2.fetchall()
				all_income_day = 0
				count = 0
				for row in fetchl2:
					if row['status'] == 1:
						count += 1
						if row['type'] == 1:
							all_income_day += round((row['cost'] / 100 * 30) / 7)
						elif row['type'] == 2:
							all_income_day += round((row['cost'] / 100 * 35) / 7)
						elif row['type'] == 3:
							all_income_day += round((row['cost'] / 100 * 40) / 7)
				if count != 0:
					bot.send_message(message.chat.id, 'Панель управления аккаунтом\n\nАктивных контрактов: %d\nОбщий суточный доход: %d ₽\n\nПодробнее в разделе:\n➕ Мои контракты' % (count, all_income_day), reply_markup=contracts(message.chat.id))
				else:
					bot.send_message(message.chat.id, 'Панель управления аккаунтом\n\n⛔ У вас нет подписанных контрактов!\n\nАктивных контрактов: 0\nОбщий суточный доход: отсутствует\n\nПодробнее в разделе:\n🔐 Доступные контракты', reply_markup=contracts(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Панель управления аккаунтом\n\n⛔ У вас нет подписанных контрактов!\n\nАктивных контрактов: 0\nОбщий суточный доход: отсутствует\n\nПодробнее в разделе:\n🔐 Доступные контракты', reply_markup=contracts(message.chat.id))
			user.position = 2
			conn.close()
		elif message.text == '⬇ Вывод' and user.clicked == 0:
			user.position = 2
			user.withdraw = 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
			query = request.select()
			fetchl = query.fetchall()
			bot.send_message(message.chat.id, 'Ваш текущий баланс: %d рублей\n\nВведите ту сумму которую хотите вывести из баланса:' % fetchl[0]['balance'], reply_markup=previous(message.chat.id))
			conn.close()
		elif len(str_find) > 0:
			user.position = 2
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=account_management(message.chat.id))
		elif message.text == '✅ История пополнений' and user.clicked == 0:
			user.clicked += 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'deposit','user_id',message.from_user.id)
			query = request.select()
			if query.rowcount == 0:
				bot.send_message(message.chat.id, 'История пополнений\n\n❌ У вас еще нет история пополнений', reply_markup=previous(message.chat.id))
			else:
				fetchl = query.fetchall()
				bot.send_message(message.chat.id, 'История пополнений\n\n')
				for row in fetchl:
					if row['status'] == 0:
						deposit_status = '❌ Не оплачена'
					else:
						deposit_status = '✅ Оплачено'
					bot.send_message(message.chat.id, 'ID операции: %d\nПлатежная система: %s\nСумма: %d\nДата: %s\n\nСтатус: %s' % (row['id'],row['payment_system'],row['cost'],row['date_it'],deposit_status), reply_markup=previous(message.chat.id))
			conn.close()
		elif message.text == '💰 История вывода' and user.clicked == 0:
			user.clicked += 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'withdraw','user_id',message.from_user.id)
			query = request.select()
			if query.rowcount == 0:
				bot.send_message(message.chat.id, 'История вывода средств\n\n❌ У вас еще не было заявок на вывод', reply_markup=previous(message.chat.id))
			else:
				fetchl = query.fetchall()
				bot.send_message(message.chat.id, 'История вывода средств\n\n')
				for row in fetchl:
					if row['status'] == 0:
						withdraw_status = '🔄 В ожидании'
					elif row['status'] == 1:
						withdraw_status = '✅ Оплачено'
					elif row['status'] == 2:
						withdraw_status = '⛔ Отменено'
					bot.send_message(message.chat.id, 'ID операции: %d\nPayeer кошелек: %s\nСумма: %d\nДата: %s\n\nСтатус: %s' % (row['id'],row['payeer'],row['cost'],row['date_it'],withdraw_status), reply_markup=previous(message.chat.id))
			conn.close()
		elif message.text == '🔐 Доступные контракты' and user.clicked == 0:
			user.clicked += 1
			user.position = 3
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			user.delete_message = message.chat.id
			user.message_id = message.message_id
			bot.send_message(message.chat.id, "📝 | Контракт «Начальный» - плюс 30% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 100 рублей до 14999 рублей.", reply_markup=inline_btn)
			user.clicked = 0
		elif message.text == '➕ Мои контракты' and user.clicked == 0:
			user.clicked += 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'contracts','user_id',message.from_user.id)
			query = request.select()
			if query.rowcount != 0:
				fetchl = query.fetchall()
				for row in fetchl:
					if row['type'] == 1:
						contract_type = 'Начальный'
						income_day = round((row['cost'] / 100 * 30) / 7)
					elif row['type'] == 2:
						contract_type = 'Стандартный'
						income_day = round((row['cost'] / 100 * 35) / 7)
					elif row['type'] == 3:
						contract_type = 'Бизнес'
						income_day = round((row['cost'] / 100 * 40) / 7)
					if row['status'] == 1:
						ts = time.time()
						date_format = '%Y-%m-%d %H:%M:%S'
						d1 = datetime.fromtimestamp(ts)
						d2 = datetime.strptime(str(row['date_start']), date_format)
						diff = d1 - d2
						contract_status = 'В процессе 🔄'
						status_working = '📈 Работает %d дней' % diff.days
					else:
						contract_status = 'Закрыт ✅'
						status_working = '📈 Работало 7 дней'
					bot.send_message(message.chat.id, 'ℹ Информация о контракте:\n\n® Тариф : %s\n📅 Срок: 7 дней\n%s\n\n💲 Доход/день : %d ₽\n💵 Заработано : %d ₽\n\n🖊 Подписан : %s\n🔒 Заканчивается : %s\n\nСтатус : %s' % (contract_type,status_working,income_day,row['working'],row['date_start'],row['date_end'],contract_status), reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Панель управления аккаунтом\n\n⛔ У вас нет подписанных контрактов!\n\nАктивных контрактов: 0\nОбщий суточный доход: отсутствует\n\nПодробнее в разделе:\n🔐 Доступные контракты', reply_markup=contracts(message.chat.id))
			user.position = 3
			conn.close()
		elif message.text == '👥 Реферальная Система' and user.clicked == 0:
			user.clicked += 1
			user.position = 2
			bot.send_message(message.chat.id, 'Направляемся․․', reply_markup=referals(message.chat.id))
		elif message.text == '➕ Моя реферальная ссылка' and user.clicked == 0:
			user.clicked += 1
			user.position = 5
			bot.send_message(message.chat.id, 'Ваша реферальная ссылка: https://t.me/Evoca_Bot?start=%d' % message.chat.id, reply_markup=previous(message.chat.id))
		elif message.text == '🤝 Мои рефералы' and user.clicked == 0:
			user.clicked += 1
			user.position = 5
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'referals','user_id',message.from_user.id)
			query = request.select()
			if query.rowcount != 0:
				fetchl = query.fetchall()
				earnings = 0
				counter = 0
				for row in fetchl:
					counter += 1
					earnings += row['earnings']
				bot.send_message(message.chat.id, 'Реферальная Система\n\nАктивных рефералов: %d\nОбщий реферальный доход: %d ₽' % (counter,earnings), reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Реферальная Система\n\n❌ У вас пока нет активных рефералов\n\nПодробнее в разделе:\n➕ Моя реферальная ссылка', reply_markup=previous(message.chat.id))
		elif message.text == '⬆ Пополнение' and user.clicked == 0:
			user.clicked += 1
			user.position = 2
			user.open_deposit = 1
			bot.send_message(message.chat.id, 'Введите сумму от 100 рублей и больше на которую хотите пополнить свой баланс:\n', reply_markup=previous(message.chat.id))
		elif user.buy_contract == 1:
			if message.text.isdigit():
				deposit_sum = int(message.text)
				if deposit_sum >= 100 and deposit_sum <= 14999:
					database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
					conn = database.connect()
					request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
					query = request.select()
					fetchl = query.fetchall()
					if fetchl[0]['balance'] >= deposit_sum:
						inline_btn = types.InlineKeyboardMarkup()
						url_button = types.InlineKeyboardButton(text="Да", callback_data="yes_ibuy")
						url_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_ibuy")
						inline_btn.row(url_button,url_button2)
						user.buy_contract = 0
						user.contract_sum = deposit_sum
						user.delete_message = message.chat.id
						user.message_id = message.message_id
						bot.send_message(message.chat.id, 'Панель управления аккаунта\n\nВы хотите заключить данный контракт на сумму %d рублей?' % deposit_sum, reply_markup=inline_btn)
					else:
						bot.send_message(message.chat.id, '❌ У вас недостаточно средств для заключение данного контракта', reply_markup=previous(message.chat.id))
				else:
					bot.send_message(message.chat.id, 'Пожалуйста введите сумму не меньше 100 и не больше 14999 рублей', reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Произошла ошибка!', reply_markup=previous(message.chat.id))
		elif user.buy_contract == 3:
			if message.text.isdigit():
				deposit_sum = int(message.text)
				if deposit_sum >= 15000 and deposit_sum <= 99999:
					database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
					conn = database.connect()
					request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
					query = request.select()
					fetchl = query.fetchall()
					if fetchl[0]['balance'] >= deposit_sum:
						inline_btn = types.InlineKeyboardMarkup()
						url_button = types.InlineKeyboardButton(text="Да", callback_data="yes_ibuy")
						url_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_ibuy")
						inline_btn.row(url_button,url_button2)
						user.buy_contract = 0
						user.contract_sum = deposit_sum
						user.delete_message = message.chat.id
						user.message_id = message.message_id
						bot.send_message(message.chat.id, 'Панель управления аккаунта\n\nВы хотите заключить данный контракт на сумму %d рублей?' % deposit_sum, reply_markup=inline_btn)
					else:
						bot.send_message(message.chat.id, '❌ У вас недостаточно средств для заключение данного контракта', reply_markup=previous(message.chat.id))
				else:
					bot.send_message(message.chat.id, 'Пожалуйста введите сумму не меньше 15000 и не больше 99999 рублей', reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Произошла ошибка!', reply_markup=previous(message.chat.id))
		elif user.buy_contract == 5:
			if message.text.isdigit():
				deposit_sum = int(message.text)
				if deposit_sum >= 100000:
					database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
					conn = database.connect()
					request = RequestDB(conn, 'accounts','user_id',message.from_user.id,0,1)
					query = request.select()
					fetchl = query.fetchall()
					if fetchl[0]['balance'] >= deposit_sum:
						inline_btn = types.InlineKeyboardMarkup()
						url_button = types.InlineKeyboardButton(text="Да", callback_data="yes_ibuy")
						url_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_ibuy")
						inline_btn.row(url_button,url_button2)
						user.buy_contract = 0
						user.contract_sum = deposit_sum
						user.delete_message = message.chat.id
						user.message_id = message.message_id
						bot.send_message(message.chat.id, 'Панель управления аккаунта\n\nВы хотите заключить данный контракт на сумму %d рублей?' % deposit_sum, reply_markup=inline_btn)
					else:
						bot.send_message(message.chat.id, '❌ У вас недостаточно средств для заключение данного контракта', reply_markup=previous(message.chat.id))
				else:
					bot.send_message(message.chat.id, 'Пожалуйста введите сумму не меньше 100000 рублей', reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Произошла ошибка!', reply_markup=previous(message.chat.id))
		elif user.open_deposit == 1:
			if message.text.isdigit():
				deposit_sum = int(message.text)
				if deposit_sum >= 100:
					inline_btn = types.InlineKeyboardMarkup()
					url_button = types.InlineKeyboardButton(text="Да", url="https://evocabot.ru?user_id=%d&amount=%d&username=%s" % (message.chat.id,deposit_sum,message.from_user.username))
					url_button2 = types.InlineKeyboardButton(text="Нет", callback_data="no_ibuy2")
					inline_btn.add(url_button)
					inline_btn.add(url_button2)
					user.open_deposit = 0
					user.deposit_sum = deposit_sum
					bot.send_message(message.chat.id, 'Панель управления аккаунта\n\nВы хотите пополнить счет на %d RUB?' % deposit_sum, reply_markup=inline_btn)
				else:
					bot.send_message(message.chat.id, 'Пожалуйста введите сумму не меньше 100 рублей', reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, 'Произошла ошибка!', reply_markup=previous(message.chat.id))
		elif message.text == '✅ Оплатил' and len(user.sum_payment) != 0 and user.clicked == 0:
			user.clicked += 1
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'deposit','comments',str("'") + user.sum_payment + str("'"),0,1)
			query = request.select()
			fetchl = query.fetchall()
			if fetchl[0]['status'] == 1:
				user.sum_payment = ''
				bot.send_message(message.chat.id, '✅ Оплата подтверждена! ваш баланс пополнился на сумму: %d рублей' % fetchl[0]['cost'], reply_markup=previous(message.chat.id))
			else:
				bot.send_message(message.chat.id, '🔄 «Ваша заявка принята на обработку если реквизиты были оплачены сумма будет начислена в течение 5 минут»', reply_markup=oplatil(message.chat.id))
		elif message.text == '🚸 Помощь':
			user.clicked += 1
			user.position = 4
			bot.send_message(message.chat.id, '1) 🔄 Рестарт - Перезапускает «Бота»\n2) 👤 Ваш аккаунт - Панель управления вашего аккаунта\n3) ⚙ Настройки - Настройи вашего аккаунта\n4) ❓ Почему мы? - Информация о проекте\n5) 📊 Развитие - О развитиях нашего проекта', reply_markup=previous(message.chat.id))
		elif message.text == '📝 Оферта':
			user.clicked += 1
			user.position = 4
			bot.send_message(message.chat.id, '🔄 В процессе разработки..', reply_markup=previous(message.chat.id))
		elif message.text == '🔐 Промо':
			user.clicked += 1
			user.position = 4
			bot.send_message(message.chat.id, '🔄 В процессе разработки..', reply_markup=previous(message.chat.id))
		elif message.text == '📢 Общий чат':
			user.position = 1
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="Открыть чат", url="https://t.me/EvocaBot")
			inline_btn.add(url_button)
			bot.send_message(message.chat.id, 'У нас есть общий чат для общение и обсуждение «Бота» с другими инвесторами и прямая связь с администрацией.\nЧто бы перейти в чат нажмите кнопку с ниже⤵', reply_markup=inline_btn)
	else:
		bot.send_message(message.chat.id, 'Что-бы начать чат введите: /start')
def keyboard(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('🔄 Рестарт')
	btn2 = types.KeyboardButton('👤 Ваш аккаунт')
	btn3 = types.KeyboardButton('⚙ Настройки')
	btn4 = types.KeyboardButton('❓ Почему мы?')
	btn5 = types.KeyboardButton('📊 Развитие')
	markup.add(btn1,btn2,btn3,btn4,btn5)
	return markup
def account(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
	conn = database.connect()
	request = RequestDB(conn, 'contracts','user_id',chatid)
	query = request.select()
	fetchl = query.fetchall()
	count = 0
	for row in fetchl:
		if row['status'] == 1:
			count += 1
	if count == 0:
		btn5 = types.KeyboardButton('📰 Контракты | Статус: Не активен')
	else:
		btn5 = types.KeyboardButton('📰 Контракты | Статус: Активен ✅')
	request = RequestDB(conn, 'accounts','user_id',chatid,0,1)
	query = request.select()
	fetchl = query.fetchall()
	btn1 = types.KeyboardButton('🛒Мой аккаунт | Баланс: %d ₽' % fetchl[0]['balance'])
	btn2 = types.KeyboardButton('⬆ Пополнение')
	btn3 = types.KeyboardButton('⬇ Вывод')
	btn6 = types.KeyboardButton('👥 Реферальная Система')
	btn4 = types.KeyboardButton('↩ Назад')
	markup.add(btn5)
	markup.add(btn1)
	markup.row(btn2,btn3)
	markup.add(btn6)
	markup.add(btn4)
	return markup
def settings(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('🚸 Помощь')
	btn2 = types.KeyboardButton('📝 Оферта')
	btn3 = types.KeyboardButton('🔐 Промо')
	btn4 = types.KeyboardButton('📢 Общий чат')
	btn5 = types.KeyboardButton('↩ Назад')
	markup.row(btn1,btn2)
	markup.add(btn3)
	markup.add(btn4)
	markup.add(btn5)
	return markup
def contracts(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('🔐 Доступные контракты')
	btn2 = types.KeyboardButton('➕ Мои контракты')
	btn3 = types.KeyboardButton('👤 Аккаунт')
	btn4 = types.KeyboardButton('↩ Назад')
	markup.row(btn1,btn2)
	markup.add(btn3)
	markup.add(btn4)
	return markup
def previous(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('↩ Назад')
	markup.add(btn1)
	return markup
def account_management(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('✅ История пополнений')
	btn2 = types.KeyboardButton('💰 История вывода')
	btn4 = types.KeyboardButton('↩ Назад')
	markup.row(btn1,btn2)
	markup.add(btn4)
	return markup
def oplatil(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('✅ Оплатил')
	btn2 = types.KeyboardButton('↩ Назад')
	markup.add(btn1)
	markup.add(btn2)
	return markup
def random_string(num):
	mystr = '#'
	for i in range(num):
		mystr += str(rnd(0,9))
		mystr += str(chr(rnd(97,122)))
	return mystr
def referals(chatid):
	global all_data
	user = all_data[chatid]
	user.clicked = 0
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	btn1 = types.KeyboardButton('➕ Моя реферальная ссылка')
	btn2 = types.KeyboardButton('🤝 Мои рефералы')
	btn3 = types.KeyboardButton('↩ Назад')
	markup.row(btn1,btn2)
	markup.add(btn3)
	return markup
@bot.callback_query_handler(lambda query: query.data == "next_contract")
def process_callback_1(query):
	global all_data
	chat_id=query.message.chat.id
	if all_data.get(chat_id) != None:
		user = all_data[chat_id]
		user.clicked = 0
		if user.current_page == 0:
			user.current_page += 1
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.buy_contract = 2
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Стандартный» - плюс 35% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 15000 рублей до 99999 рублей.", reply_markup=inline_btn)
		elif user.current_page == 1:
			user.current_page += 1
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.buy_contract = 4
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Бизнес» - плюс 40% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 100000 рублей до ∞ рублей.", reply_markup=inline_btn)
		else:
			user.current_page = 0
			user.buy_contract = 0
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Начальный» - плюс 30% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 100 рублей до 14999 рублей.", reply_markup=inline_btn)
@bot.callback_query_handler(lambda query: query.data == "previous_contract")
def process_callback_2(query):
	global all_data
	chat_id=query.message.chat.id
	if all_data.get(chat_id) != None:
		user = all_data[chat_id]
		user.clicked = 0
		if user.current_page == 0:
			user.current_page = 2
			user.buy_contract = 4
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Бизнес» - плюс 40% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 100000 рублей до ∞ рублей.", reply_markup=inline_btn)
		elif user.current_page == 2:
			user.current_page = 1
			user.buy_contract = 2
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Стандартный» - плюс 35% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 15000 рублей до 99999 рублей.", reply_markup=inline_btn)
		else:
			user.current_page = 0
			bot.delete_message(user.delete_message, user.message_id + 1)
			user.delete_message = chat_id
			user.buy_contract = 0
			user.message_id = query.message.message_id
			inline_btn = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="⬅", callback_data="previous_contract")
			url_button2 = types.InlineKeyboardButton(text="➕", callback_data="buy_contract")
			url_button3 = types.InlineKeyboardButton(text="➡", callback_data="next_contract")
			inline_btn.row(url_button,url_button2,url_button3)
			bot.send_message(chat_id, "📝 | Контракт «Начальный» - плюс 30% к депозиту.\n🕔 | Продолжительность контракта - 7 дней.\n💰 | Сумма взноса от 100 рублей до 14999 рублей.", reply_markup=inline_btn)
@bot.callback_query_handler(lambda query: query.data == "buy_contract")
def process_callback_3(query):
	global all_data
	chat_id=query.message.chat.id
	if all_data.get(chat_id) != None:
		user = all_data[chat_id]
		user.clicked = 0
		if user.delete_message != 0:
			bot.delete_message(user.delete_message, user.message_id + 1)
			if user.buy_contract == 0:
				user.buy_contract = 1
				bot.send_message(chat_id, 'Введите ту сумму на которую хотите заключить контракт сумма должна быть не меныше 100 рублей и не больше 14999 рублей.', reply_markup=previous(chat_id))
			elif user.buy_contract == 2:
				user.buy_contract = 3
				bot.send_message(chat_id, 'Введите ту сумму на которую хотите заключить контракт сумма должна быть не меныше 15000 рублей и не больше 99999 рублей.', reply_markup=previous(chat_id))
			elif user.buy_contract == 4:
				user.buy_contract = 5
				bot.send_message(chat_id, 'Введите ту сумму на которую хотите заключить контракт сумма должна быть не меныше 100000 рублей и не больше ∞', reply_markup=previous(chat_id))
@bot.callback_query_handler(lambda query: query.data == "no_ibuy2")
def process_callback_4(query):
	global all_data
	chat_id=query.message.chat.id
	if all_data.get(chat_id) != None:
		user = all_data[chat_id]
		user.clicked = 0
		user_id = user.user_id
		if user.deposit_sum != 0:
			user.deposit_sum = 0
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'accounts','user_id',user_id,0,1)
			query = request.select()
			fetchl = query.fetchall()
			bot.send_message(chat_id, 'Направляемся․․', reply_markup=account(user_id))
# @bot.callback_query_handler(lambda query: query.data == "yes_ibuy2")
# def process_callback_5(query):
# 	global all_data
# 	chat_id=query.message.chat.id
# 	if all_data.get(chat_id) != None:
# 		user = all_data[chat_id]
# 		user.clicked = 0
# 		user_id = user.user_id
# 		if user.deposit_sum != 0:
# 			rand_str= random_string(4)
# 			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
# 			conn = database.connect()
# 			arr_insert = str(user_id) + str(",") + str(user.deposit_sum) + str(",") + str("'") + str("Payeer") + str("'") + str(",") + str("'") + str(rand_str) + str("'") + str(",") + str(0)
# 			request = RequestDB(conn, 'deposit','user_id,cost,payment_system,comments,status',arr_insert)
# 			query = request.insert()
# 			conn.commit()
# 			request = RequestDB(conn, 'deposit','comments',str("'") + rand_str + str("'"),0,1)
# 			query = request.select()
# 			fetchl = query.fetchall()
# 			user.deposit_sum = 0
# 			user.sum_payment = rand_str
# 			user.position = 2
# 			bot.send_message(chat_id, "Пополнение баланса №%d\nОперация создана: %s\n\nСумма : %dр\nРеквизиты для оплаты: P1017902517\nС Комментарием: %s\n\nОБЯЗАТЕЛЬНО!\nПри переводе суммы указывайте комментарии.\n\nВнимание!\nНачисление на счёт производится в течение 5 минут." % (fetchl[0]['id'],fetchl[0]['date_it'],fetchl[0]['cost'],rand_str), reply_markup=oplatil(user_id))
# 			conn.close()
@bot.callback_query_handler(lambda query: query.data == "yes_ibuy")
def process_callback_6(query):
	global all_data
	chat_id=query.message.chat.id
	if all_data.get(chat_id) != None:
		user = all_data[chat_id]
		user.clicked = 0
		if user.contract_sum != 0:
			database = ConnectDB('45.13.252.1','u301024735_botter','botinbot2019','u301024735_botter')
			conn = database.connect()
			request = RequestDB(conn, 'accounts','user_id',chat_id,0,1)
			query = request.select()
			if query.rowcount != 0:
				fetchl = query.fetchall()
				if fetchl[0]['balance'] >= user.contract_sum:
					user_balance = fetchl[0]['balance']
					new_balance = user_balance - user.contract_sum
					ts = time.time() + 604800
					st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
					if user.contract_sum >= 100 and user.contract_sum <= 14999:
						types = 1
					elif user.contract_sum >= 15000 and user.contract_sum <= 99999:
						types = 2
					elif user.contract_sum >= 100000:
						types = 3
					request3 = RequestDB(conn, 'accounts','balance',new_balance,'user_id',chat_id)
					request3.update()
					conn.commit()
					arr_insert = str(chat_id) + str(",") + str(user.contract_sum) + str(",") + str(0) + str(",") + str("'") + str(st) + str("'") + str(",") + str(1) + str(",") + str(types)
					request2 = RequestDB(conn, 'contracts','user_id,cost,working,date_end,status,type',arr_insert)
					request2.insert()
					conn.commit()
					bot.delete_message(user.delete_message, user.message_id + 1)
					user.contract_sum = 0
					user.buy_contract = 0
					bot.send_message(chat_id, '✅ Поздравляем! Вы успешно заключили новый контракт', reply_markup=account(chat_id))
				else:
					user.buy_contract = 0
					bot.send_message(chat_id, '❌ У вас недостаточно средств для заключение данного контракта', reply_markup=previous(chat_id))
			conn.close()
# @bot.callback_query_handler(lambda query: query.data == "start_system")
# def process_callback_6(query):
# 	global all_data
# 	chat_id=query.message.chat.id
# 	if all_data['started'] == 0:
# 		all_data['started'] = 1
# 		bot.delete_message(user.delete_message, user.message_id + 1)
# 		user.delete_message = chat_id
# 		user.message_id = query.message.message_id
# 		bot.send_message(chat_id, 'Направляемся․․', reply_markup=keyboard())
while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        time.sleep(15)