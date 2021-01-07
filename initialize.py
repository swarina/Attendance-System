import sqlite3
import os
import shutil


def init_():
    try:
        shutil.rmtree("Dataset/")
    except OSError as error:
        pass
    try:
        shutil.rmtree("Trained/")
    except OSError as error:
        pass
    try:
        os.remove("database.db")
        print("Cleaned Successfully")
    except OSError as error:
        print("No Previous Database Found")

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE students (
	        roll_no integer,
	        name varchar(100)
	    )
	    """)
    conn.commit()

    # date format: ddmmyyyy
    # integer student
    cur.execute("""CREATE TABLE attendance (
	        date char(8)
	    )
	    """)
    conn.commit()
    os.mkdir("Dataset")
    os.mkdir("Trained")
    print("Created Database Successfully\n")


if __name__ == '__main__':
    print("This module can't be run directly! :(\n")
