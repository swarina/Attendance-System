import sqlite3

def init_(): 
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	    
	cur.execute("""CREATE TABLE students (
	        roll_no integer,
	        name varchar(100)
	    )
	    """)
	conn.commit()

	#date format: ddmmyyyy
	# integer student
	cur.execute("""CREATE TABLE attendance (
	        date char(8)
	    )
	    """)
	conn.commit()
if __name__ == '__main__':
	print("This module can't be run directly! :(\n")
