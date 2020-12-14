from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError,NumberRange
from flask_wtf.file import FileField,FileAllowed

class RegisterForm(FlaskForm):
	Username=StringField('Username',validators=[DataRequired(),Length(min=2, max=15)])
	Email=StringField('Email',validators=[DataRequired(),Email()])
	Password=PasswordField('Password',validators=[DataRequired()])
	Phno=StringField('Phono num' ,validators=[DataRequired(),Length(min=10, max=12)])
	ConformPassword=PasswordField('ConformPassword',validators=[DataRequired(),EqualTo("Password")])
	Address=TextAreaField('Address',validators=[DataRequired()])
	Submit=SubmitField('Sign IN')


	def validate_user(self,Username):
		user=User.query.filter_by(Username=Username.data).first()
		if user:
			raise ValidationError('this Username is Taken try another one')

	def validate_email(self,Email):
		email=User.query.filter_by(Email=Email.data).first()
		if email:
			raise ValidationError('this Email is Taken try another one')

	

class LoginForm(FlaskForm):
	Email=StringField('Email',validators=[DataRequired(),Email()])
	Password=PasswordField('Password',validators=[DataRequired()])
	Submit=SubmitField('Login')



class SellForm(FlaskForm):
	Username=StringField('Username',validators=[DataRequired(),Length(min=2, max=15)])
	Email=StringField('Email',validators=[DataRequired(),Email()])
	Address=TextAreaField('Address',validators=[DataRequired()])
	Phno=StringField('Phono num' ,validators=[DataRequired(),Length(min=10, max=12)])
	FrontImg=FileField('FrontImg',validators=[FileAllowed(['jpg','png'])])
	BackImg=FileField('BackImg',validators=[FileAllowed(['jpg','png'])])
	RSImg=FileField('Right_side_Img',validators=[FileAllowed(['jpg','png'])])
	LSImg=FileField('Left_Side_Img',validators=[FileAllowed(['jpg','png'])])
	Milage=FileField('Milage',validators=[FileAllowed(['pdf'])])
	VIN=FileField('VIN',validators=[FileAllowed(['pdf'])])
	Finance=FileField('Fianace',validators=[FileAllowed(['pdf'])])
	Model=StringField('Model',validators=[DataRequired()])
	Company=StringField('Company',validators=[DataRequired()])
	Colour=StringField('Colour',validators=[DataRequired()])
	Submit=SubmitField('Post')


	def validate_user(self,Username):
		user=User.query.filter_by(Username=Username.data).first()
		if user:
			raise ValidationError('this Username is Taken try another one')

	def validate_email(self,Email):
		email=User.query.filter_by(Email=Email.data).first()
		if email:
			raise ValidationError('this Email is Taken try another one')

	