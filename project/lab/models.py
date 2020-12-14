from lab import db,login
from flask_login import UserMixin


@login.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model,UserMixin):
	id=db.Column(db.Integer,primary_key=True)
	Username=db.Column(db.String(100), unique=True, nullable=False)
	Email=db.Column(db.String(120), unique=True, nullable=False)
	Password=db.Column(db.Text, nullable=False)
	count=db.Column(db.Integer,nullable=False, default=0)
	phone=db.Column(db.String(13),nullable=False,unique=True)
	Address=db.Column(db.String(100), nullable=False)
	buyer=db.relationship('Buyers', backref='buyer',lazy=True )
	seller=db.relationship('Sellers', backref='seller',lazy=True )

	
	def __repr__(self):
		return(f'{self.Username},{self.Email},{self.Password}')

class Buyers(db.Model):
	buy_id=db.Column(db.Integer,primary_key=True)
	User_i=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	vec_buyer=db.relationship('Vehicle', backref='vec_buyer',lazy=True )
	def __repr__(self):
		return(f'{self.User_id},{self.buy_id}')
	
	
class Sellers(db.Model):
	sel_id=db.Column(db.Integer,primary_key=True)
	User_i=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	vec_seller=db.relationship('Vehicle', backref='vec_seller',lazy=True )
	def __repr__(self):
		return(f'{self.User_i},{self.sel_id}')
		
class Vehicle(db.Model):
	vec_id=db.Column(db.Integer,primary_key=True)
	Image_Front=db.Column(db.String(120),default='default.jpg',nullable=False)
	Image_Back=db.Column(db.String(120),default='default.jpg',nullable=False)
	Image_rside=db.Column(db.String(120),default='default.jpg',nullable=False)
	Image_lside=db.Column(db.String(120),default='default.jpg',nullable=False)
	
	Company=db.Column(db.String(100), nullable=False)
	Model=db.Column(db.String(100), nullable=False)
	Colour=db.Column(db.String(100), nullable=False)
	check=db.relationship('Check', backref='check',lazy=True )
	buyer_id=db.Column(db.Integer,db.ForeignKey('buyers.buy_id'))
	seller_id=db.Column(db.Integer,db.ForeignKey('sellers.sel_id'),nullable=False)
	def __repr__(self):
		return(f'{self.vec_id},{self.buyer_id},{self.seller_id}')



class Check(db.Model):
	ckeck_id=db.Column(db.Integer,primary_key=True)
	cvec_id=db.Column(db.Integer,db.ForeignKey('vehicle.vec_id'),nullable=False)
	mil=db.Column(db.String(120),default='default.jpg',nullable=False)
	vin=db.Column(db.String(120),default='default.jpg',nullable=False)
	fin=db.Column(db.String(120),default='default.jpg',nullable=False)


	def __repr__(self):
		return(f'{self.ckeck_id},{self.cvec_id}')



