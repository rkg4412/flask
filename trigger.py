from lab import db,login,app
from flask_login import UserMixin,current_user
from sqlalchemy.orm import backref
from datetime import datetime
from sqlalchemy import create_engine
from lab.models import User

engine = create_engine('mysql://root:roottiger@localhost/flaskdb')



class trigger():
	def insert_user_tri():
		with engine.connect() as connection:
			result = connection.execute('''CREATE trigger act_insert
    				AFTER insert
    				on user for each row 
                	BEGIN
                	call insert_user();
                	END;''')
			result.close()
	def update_user_tri():
		with engine.connect() as connection:
			result = connection.execute('''CREATE trigger act_update
    				AFTER update
    				on user for each row 
                	BEGIN
                	call update_user();
                	END;''')
			result.close()
	def insert_vec_tri():
		with engine.connect() as connection:
			result = connection.execute('''CREATE trigger vec_insert
    				AFTER insert
    				on vehicle for each row 
                	BEGIN
                	call insert_vec();
                	END;''')
			result.close()
	def update_vec_tri():
		with engine.connect() as connection:
			result = connection.execute('''CREATE trigger vec_update
    				AFTER update
    				on vehicle for each row 
                	BEGIN
                	call update_vec();
                	END;''')
			result.close()


trigger.insert_user_tri()
trigger.update_user_tri()
trigger.insert_vec_tri()
trigger.update_vec_tri()