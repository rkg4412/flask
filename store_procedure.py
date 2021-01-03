from lab import db,login,app
from flask_login import UserMixin,current_user
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy import create_engine

engine = create_engine('mysql://root:roottiger@localhost/flaskdb')

class procedure():
	def insert_user():
		x=datetime.now()
		print(x)
		with engine.connect() as connection:
			result = connection.execute('''CREATE PROCEDURE insert_user() 
                BEGIN 
                INSERT INTO flaskdb.activity (at ,action,time) VALUES("User","Insert",%s);  
                END''',(str(x)))
			result.close()
	def update_user():
		x=datetime.now()
		print(x)
		with engine.connect() as connection:
			result = connection.execute('''CREATE PROCEDURE update_user() 
                BEGIN 
                INSERT INTO flaskdb.activity (at ,action,time) VALUES("User","Update",%s);  
                END''',(str(x)))
			result.close()
	def insert_vec():
		x=datetime.now()
		print(x)
		with engine.connect() as connection:
			result = connection.execute('''CREATE PROCEDURE insert_vec() 
                BEGIN 
                INSERT INTO flaskdb.activity (at ,action,time) VALUES("Vechicle","Insert",%s);  
                END''',(str(x)))
			result.close()
	def update_vec():
		x=datetime.now()
		print(x)
		with engine.connect() as connection:
			result = connection.execute('''CREATE PROCEDURE update_vec() 
                BEGIN 
                INSERT INTO flaskdb.activity (at,action,time) VALUES("Vechicle","Update",%s);  
                END''',(str(x)))
			result.close()


procedure.insert_user()
procedure.update_user()
procedure.insert_vec()
procedure.update_vec()