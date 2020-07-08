import mysql.connector
import pandas as pd
import sys
import CONF

class Extract_SQL:
	def __init__(self):
		self.host=CONF.sqlInfo['host']
		self.user=CONF.sqlInfo['username']
		self.password=CONF.sqlInfo['password']
		self.database=CONF.sqlInfo['database']
	def fetch(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
		else:
			mark = ' where ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
		try:
			mycursor.execute('select * from '+ CONF.currLogTable + mark +' for update')
			myresult = mycursor.fetchall()
			if myresult == []:
				return [["Null", "Null", "Null", "Null", "Null"]]
			return myresult
		except mysql.connector.Error as e:
			print(e)
		finally:
			mycursor.close()
			mydb.close()

	def fetchCount(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
			mark1 = ''
		else:
			mark = ' where ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
			mark1 = ' and ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
		try:
			mycursor.execute('select COUNT('+CONF.columns[0]+') from '+ CONF.accLogTable + mark +' for update')
			myresult1 = mycursor.fetchall()[0][0]
			mycursor.execute('select count('+CONF.columns[0]+') from ' + CONF.accLogTable + ' where '+CONF.columns[2]+' = \"FAIL\"' + mark1 +' for update')
			myresult2 = mycursor.fetchall()[0][0]
			mycursor.execute('select count('+CONF.columns[0]+') from '+ CONF.currLogTable + mark +' for update')
			myresult3 = mycursor.fetchall()[0][0]
			mycursor.execute('select count('+CONF.columns[0]+') from '+ CONF.currLogTable +' where '+CONF.columns[2]+' = \"FAIL\"'+ mark1 +' for update')
			myresult4 = mycursor.fetchall()[0][0]
			return [myresult1, myresult2, myresult3, myresult4]

		except mysql.connector.Error as e:
			print(e)

		finally:
			mycursor.close()
			mydb.close()

	def fetchDateAndFail(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
		else:
			mark = ' and ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
		try:
			mycursor.execute('select '+CONF.columns[4]+',count('+CONF.columns[4]+') from '+CONF.accLogTable+' where '+CONF.columns[2]+' = "FAIL"'+mark+' group by '+CONF.columns[4]+' for update')
			myresult = mycursor.fetchall()
			return myresult
		except mysql.connector.Error as e:
			print(e)

		finally:
			mycursor.close()
			mydb.close()

	def fetchSectionFail(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
		else:
			mark = ' and ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
		try:
			mycursor.execute('select '+CONF.columns[0]+',count('+CONF.columns[4]+') from '+CONF.accLogTable+' where '+CONF.columns[2]+' = "FAIL"'+mark+' group by '+CONF.columns[0]+' for update')
			myresult = mycursor.fetchall()
			return myresult
		except mysql.connector.Error as e:
			print(e)

		finally:
			mycursor.close()
			mydb.close()

	def fetchCaseName(self, data):
		mydb = mysql.connector.connect(
			host=self.host,
			user=self.user,
			password=self.password,
			database=self.database
			)
		mycursor = mydb.cursor()
		if data == 0:
			mark = ''
		else:
			mark = ' and ' + CONF.columns[0] + ' = ' + '\"' + CONF.sectionNames[data-1] + '\"'
		try:
			mycursor.execute('select '+CONF.columns[1]+',count('+CONF.columns[4]+') from '+CONF.accLogTable+' where '+CONF.columns[2]+' = "FAIL"'+mark+' group by '+CONF.columns[1]+' for update')
			myresult = mycursor.fetchall()
			return dict(myresult)
		except mysql.connector.Error as e:
			print(e)

		finally:
			mycursor.close()
			mydb.close()







if __name__ == '__main__':
	exsql = Extract_SQL()
	res = exsql.fetchSectionFail(0)
	print(res)


