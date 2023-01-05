sig = 2

numb = (1234,)
tup = (20, 30)

def minus_n(sig, numb, tupp):
	sig = sig
	numb = numb
	
	tup = ()
	
	for i in tupp:
		n = i-(i*2)
		n = (n,)
		tup = tup+n
		#print(tup)
		
	data = numb+tup
	print(data)
	if sig == 1:
		print('yes')
	else:
		print('no')
		
		
minus_n(sig, numb, tup)

# функции джоин передается значения из нужной таблицы.

##### функция отним. #####

def minus_n_db():
	
	conn = sqlite3.connect("sqlite_python.db")
	cursor = conn.cursor()
	
	data = ("""SELECT * FROM loss WHERE rowid>0 ORDER BY rowid DESC LIMIT 1""")
	cursor.execute(data)
	records = cursor.fetchall()
	#print(records)
	time.sleep(1)
	
	cursor.executemany("INSERT INTO main_file VALUES (?, ?, ?, ?, ?)", records)
	conn.commit()
	time.sleep(1)
	
	number = ('''SELECT index_db FROM main_file''')
	cursor.execute(number)
	number = cursor.fetchall()
	number = number[0]
	
	meet = ('''SELECT meet FROM main_file''')
	cursor.execute(meet)
	meet = cursor.fetchall()
	n1 = meet[0]
	n1 = n1[0]
	n2 = meet[1]
	n2 = n2[0]
	meet = n1-n2
	meet = (meet,)

	

	amount = number+meet
	print(amount)

#minus_n_db()


#### add to loss table ####

number_loss = (1498,)
val_loss = (150.100, 250.002, 180.030, 230.444)

def add_n_to_db_loss(number_loss, val_loss):
	number_loss = number_loss
	val_loss = val_loss
	almount2 = number_loss + val_loss
	val = []
	val.append(almount2)
	conn = sqlite3.connect("sqlite_python.db")
	cursor = conn.cursor()
	cursor.executemany("INSERT INTO loss VALUES (?,?,?,?,?)", val)
	### 

	conn.commit()

#add_n_to_db_loss(number_loss, val_loss)

###### функция сцепки #######

def join_db():
	conn = sqlite3.connect("sqlite_python.db")
	cursor = conn.cursor()

	data = ("""SELECT * FROM profit WHERE rowid>0 ORDER BY rowid DESC LIMIT 1""")
	cursor.execute(data)
	records = cursor.fetchall()
	# print(records)
	time.sleep(1)
	cursor.executemany("INSERT INTO main_file VALUES (?, ?, ?, ?, ?)", records)
	conn.commit()
	time.sleep(1)
	##########
	number = ('''SELECT index_db FROM main_file''')
	cursor.execute(number)
	number = cursor.fetchall()
	number = number[0]

	meet = ('''SELECT sum(meet) FROM main_file''')
	cursor.execute(meet)
	meet = cursor.fetchall()
	meet = meet[0]

	fish = ('''SELECT sum(fish) FROM main_file''')
	cursor.execute(fish)
	fish = cursor.fetchall()
	fish = fish[0]

	butter = ('''SELECT sum(butter) FROM main_file''')
	cursor.execute(butter)
	butter = cursor.fetchall()
	butter = butter[0]

	poteito = ('''SELECT sum(poteito) FROM main_file''')
	cursor.execute(poteito)
	poteito = cursor.fetchall()
	poteito = poteito[0]

	amount = number + meet + fish + butter + poteito
	vall = []
	vall.append(amount)

	cursor.executemany("INSERT INTO main_file VALUES (?,?,?,?,?)", vall)

	conn.commit()
	##########
	time.sleep(1)
	row = ("""SELECT rowid FROM main_file WHERE rowid>0 ORDER BY rowid LIMIT 2""")
	cursor.execute(row)
	rows = cursor.fetchall()
	row1 = rows[0]
	row2 = rows[1]
	delete_row = ("""DELETE FROM main_file WHERE rowid = ?""")
	cursor.execute(delete_row, (row1))
	conn.commit()
	delete_row = ("""DELETE FROM main_file WHERE rowid = ?""")
	cursor.execute(delete_row, (row2))
	conn.commit()

# join_db()

