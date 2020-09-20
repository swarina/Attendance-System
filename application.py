import sqlite3
import os
from subprocess import Popen
from datetime import date
import initialize, detection, train, recognition

today = date.today()
date_today = today.strftime("%d%m%Y")

print("List of Valid Operations:\n")
print("1. Create a database")
print("2. Add a student")
print("3. Train the model")
print("4. Scan face for attendance")
print("5. Check Attendance")
print("6. View Database")
to_do = int(input("\n Enter Valid number: "))

if to_do == 1:
	initialize.init_()
elif to_do == 2:
	detection.detect()
elif to_do == 3:
	train.train()
elif to_do == 4:
	recognition.recognise()
elif to_do == 5:
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	roll_no = input("\nEnter Roll no. :")
	cur.execute("SELECT date FROM attendance WHERE _{s_roll_no}=1".format(s_roll_no=roll_no))
	# print(cur.fetchall())
	presents = len(cur.fetchall())
	cur.execute("SELECT * FROM attendance")
	total = len(cur.fetchall())
	print(str(presents) + '/' + str(total))
else:
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM attendance")
	items = cur.fetchall()
	for _ in items:
    		print(_)

    	
