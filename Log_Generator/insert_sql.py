import mysql.connector
import pandas as pd
import sys
import CONF

class Manipulate_SQL:
	def __init__(self):
		self.host=CONF.sqlInfo['host']
		self.user=CONF.sqlInfo['username']
		self.password=CONF.sqlInfo['password']
		self.database=CONF.sqlInfo['database']
	def insert(self, tableName, sqlArgsList):
		if len(sqlArgsList) != 5 or tableName not in [CONF.currLogTable, CONF.accLogTable]:
			print("Error>参数有误")
			return
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		#mydb.start_transaction(isolation_level='SERIALIZABLE')
		mycursor = mydb.cursor()
		try:
			mycursor.execute('insert into ' + tableName + ' values(\"' + sqlArgsList[0] + '\",\"' + sqlArgsList[1] + '\",\"' + sqlArgsList[2] + '\",\"' + sqlArgsList[3] + '\",\"' + sqlArgsList[4] + '\")')
			mydb.commit()
		except mysql.connector.Error as e:
			print(e)
		finally:
			mycursor.close()
			mydb.close()
	def truncate(self, table):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		#mydb.start_transaction(isolation_level='SERIALIZABLE')
		mycursor = mydb.cursor()
		try:
			mycursor.execute("truncate "+table)
			mydb.commit()
		except mysql.connector.Error as e:
			print(e)
		finally:
			mycursor.close()
			mydb.close()
	def insertFail(self, tableName, sqlArgsList):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		#mydb.start_transaction(isolation_level='SERIALIZABLE')
		mycursor = mydb.cursor()
		try:
			mycursor.execute('insert into ' + tableName + ' values(\"' + sqlArgsList[0] + '\",\"' + sqlArgsList[1] + '\",\"' + 'FAIL' + '\",\"' + sqlArgsList[3] + '\",\"' + sqlArgsList[4] + '\")')
			mydb.commit()
		except mysql.connector.Error as e:
			print(e)
		finally:
			mycursor.close()
			mydb.close()



