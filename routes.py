from flask import Flask,render_template,url_for,redirect,flash,request,abort
from lab.forms import RegisterForm,LoginForm,SellForm,UpdateForm,updateUserForm
from lab import app, bcrpyt,db,login
from lab.models import User,Buyers,Sellers,Vehicle,Check
from flask_login import login_user,current_user,login_required,logout_user
import secrets
import os



@app.route('/')
@app.route('/home')
def home():
	vec=Vehicle.query.all()
	return render_template('home.html',vec=vec,sep=os.sep)


@app.route('/register', methods=["POST","GET"])
def register_from():
	form=RegisterForm()
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	print(form.errors)
	if form.validate_on_submit():
		h_password=bcrpyt.generate_password_hash(form.Password.data).decode('utf-8')
		print(form.Phno.data)
		user=User(Username=form.Username.data,Email=form.Email.data,Password=h_password,Address=form.Address.data,phone=form.Phno.data)
		db.session.add(user)
		db.session.commit()
		flash("Your account is been created ","success")
		return redirect(url_for('home'))
	print(form.errors)	
	return render_template('register.html',title="Register Form",form=form)

@app.route('/login', methods=["POST","GET"])
def login_form():
	form=LoginForm()
	if form.validate_on_submit():
		print(form.errors)
		user=User.query.filter_by(Email=form.Email.data).first()
		print(user)
		if user and bcrpyt.check_password_hash(user.Password, form.Password.data):
			login_user(user)
			next_page=request.args.get('next')
			print(request)
			print(request.args)
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
			return redirect(url_for('home'))
		else:
			flash("Your entered details are incorrect")
	return render_template("login.html",form=form,title="Login")





def save(n,form_pic,sel_id):
	hex_name=secrets.token_hex(8)
	f_name,f_ext=os.path.splitext(form_pic.filename)
	if n==1:
		pic_name=hex_name+"first"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name

	elif n==2:
		pic_name=hex_name+"back"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name
	elif n==3:
		pic_name=hex_name+"right"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name
	elif n==4:
		pic_name=hex_name+"left"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name
	elif n==5:
		pic_name=hex_name+"Milage"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name
	elif n==6:
		pic_name=hex_name+"VIN"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name
	elif n==7:
		pic_name=hex_name+"Finance"+f_ext
		pic_path=os.path.join(app.root_path+'\\static\\pic\\',pic_name)
		form_pic.save(pic_path)
		return pic_name


@app.route('/sell', methods=["POST","GET"])
@login_required
def Sellform():
	form=SellForm()
	if form.validate_on_submit():
		m=os.sep.join([app.root_path,'static','pic'])
		if os.path.exists(m)==False:
			os.makedirs(m)
		if form.FrontImg.data:
			F=save(1,form.FrontImg.data,current_user.id)
		if form.BackImg.data:
			B=save(2,form.BackImg.data,current_user.id)
		if form.RSImg.data:
			L=save(3,form.RSImg.data,current_user.id)
		if form.LSImg.data:
			R=save(4,form.LSImg.data,current_user.id)
		if form.Milage.data:
			M=save(5,form.Milage.data,current_user.id)
		if form.VIN.data:
			V=save(6,form.VIN.data,current_user.id)
		if form.Finance.data:
			Fi=save(7,form.Finance.data,current_user.id)
		if Sellers.query.filter_by(User_i=current_user.id).first()==None:
			seller=Sellers(User_i=current_user.id)
			db.session.add(seller)
			db.session.commit()

		
		for i in current_user.seller:
			m=i.sel_id
		v1=Vehicle(Company=form.Company.data,Model=form.Model.data,Colour=form.Colour.data,Image_Front=F,Image_Back=B,Image_lside=L,Image_rside=R,seller_id=m)
		db.session.add(v1)
		db.session.commit()
		sel=Sellers.query.get(m)
		t=len(sel.vec_seller)
		print(t)
		count=0
		for z in sel.vec_seller:
			if count==t-1:
				xi=z.vec_id
			count=count+1
		c1=Check(mil=M,vin=V,fin=Fi,cvec_id=xi)
		db.session.add(c1)
		db.session.commit()
		flash("Your Vehicle has been recorded","success")
		return redirect(url_for('home'))
	elif request.method=="GET":
		form.Username.data=current_user.Username
		form.Address.data=current_user.Address
		form.Email.data=current_user.Email
		form.Phno.data=current_user.phone

	return render_template('sell.html',title="Seller details",form=form)


@app.route('/logout', methods=["POST","GET"])
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/vel/<int:vec_id>', methods=["POST","GET"])
@login_required
def vec(vec_id):
	vec=Vehicle.query.get(vec_id)
	
	m=os.sep
	FI=url_for('static',filename=f'pic/{vec.Image_Front}')
	BI=url_for('static',filename=f'pic/{vec.Image_Back}')
	LI=url_for('static',filename=f'pic/{vec.Image_rside}')
	RI=url_for('static',filename=f'pic/{vec.Image_lside}')
	sel=Sellers.query.get(vec.seller_id)
	user=User.query.filter_by(id=sel.User_i).first()
	ch=Check.query.filter_by(cvec_id=vec_id).first()
	Fin=url_for('static',filename=f'pic/{ch.fin}')
	vin=url_for('static',filename=f'pic/{ch.vin}')
	mil=url_for('static',filename=f'pic/{ch.mil}')
	buy=Buyers.query.get(vec.buyer_id)
	return render_template('vecdetails.html',vec=vec,title="Details" ,front=FI,back=BI,left=LI,right=RI,user=user,fin=Fin,vin=vin,mil=mil,seller=sel,buy=buy)


@app.route('/vel/<int:vec_id>/update', methods=["POST","GET"])
@login_required
def vec_update(vec_id):
	form=UpdateForm()
	vec=Vehicle.query.get_or_404(vec_id)
	ch=Check.query.filter_by(cvec_id=vec_id).first()
	if current_user.s_user.sel_id!=vec.seller_id:
		abort(403)
	if form.validate_on_submit():
		if form.FrontImg.data:
			Fu=save(1,form.FrontImg.data,current_user.id)
			vec.Image_Front=Fu
		if form.BackImg.data:
			Bu=save(2,form.BackImg.data,current_user.id)
			vec.Image_Back=Bu
		if form.RSImg.data:
			Ru=save(3,form.RSImg.data,current_user.id)
			vec.Image_rside=Ru

			
		if form.LSImg.data:
			Lu=save(4,form.LSImg.data,current_user.id)
			vec.Image_lside=Lu
		if form.Milage.data:
			Mu=save(5,form.Milage.data,current_user.id)
			ch.mil=Mu
		if form.VIN.data:
			Vu=save(6,form.VIN.data,current_user.id)
			ch.vin=Vu
		if form.Finance.data:
			Fiu=save(7,form.Finance.data,current_user.id)
			ch.fin=Fiu
		db.session.commit()
		
		flash("your Vehicle details is updated")
		return redirect(url_for('home'))
	elif request.method=="GET":
		form.Company.data=vec.Company
		form.Model.data=vec.Model
		form.Colour.data=vec.Colour
	FI=url_for('static',filename=f'pic/{vec.Image_Front}')
	BI=url_for('static',filename=f'pic/{vec.Image_Back}')
	RI=url_for('static',filename=f'pic/{vec.Image_rside}')
	LI=url_for('static',filename=f'pic/{vec.Image_lside}')
	Fin=url_for('static',filename=f'pic/{ch.fin}')
	vin=url_for('static',filename=f'pic/{ch.vin}')
	mil=url_for('static',filename=f'pic/{ch.mil}')
	return render_template("details_update.html" ,form=form,title="Update",front=FI,back=BI,left=LI,right=RI,fin=Fin,vin=vin,mil=mil)

@app.route('/vel/<int:vec_id>/book', methods=["POST","GET"])
@login_required
def vec_book(vec_id):
	vec=Vehicle.query.get_or_404(vec_id)
	if current_user.s_user != None:
		if current_user.s_user.sel_id==vec.seller_id:
			abort(403)
	vec=Vehicle.query.get_or_404(vec_id)
	b1=Buyers.query.filter_by(User_i=current_user.id).first()
	if b1==None:
		buy=Buyers(User_i=current_user.id)
		db.session.add(buy)
		db.session.commit()
		vec.buyer_id=buy.buy_id
		db.session.commit()
	else:
		vec.buyer_id=b1.buy_id
		db.session.commit()
	flash('Your booking Message is delivered to the seller')
	return redirect(url_for('home'))


@app.route('/vel/<int:vec_id>/Register', methods=["POST","GET"])
@login_required
def vec_Register(vec_id):
	vec=Vehicle.query.get_or_404(vec_id)
	if current_user.s_user.sel_id!=vec.seller_id:
		abort(403)
	if vec.count==1 and vec.buyer_id==None:
		abort(403)
	vec.count=1
	db.session.commit();
	flash('Your Vehicle has been Register')
	return redirect(url_for('home'))



@app.route('/vel/<int:vec_id>/Withdraw', methods=["POST","GET"])
@login_required
def vec_Withdraw(vec_id):
	vec=Vehicle.query.get_or_404(vec_id)
	if current_user.s_user.sel_id!=vec.seller_id:
		abort(403)
	if vec.count==1:
		abort(403)
	vec.count=1
	vec.buyer_id=None
	db.session.commit();
	flash('Your Vehicle has been Withdraw')
	return redirect(url_for('home'))


@app.route('/profile', methods=["POST","GET"])
@login_required
def profile():
	user=User.query.get_or_404(current_user.id)
	if current_user.s_user==None:
		vec_sel=None
	else:
		vec_sel=Vehicle.query.filter_by(seller_id=current_user.s_user.sel_id)
	
	if current_user.b_user==None:
		vec_buy=None
	else:
		vec_buy=Vehicle.query.filter_by(buyer_id=current_user.b_user.buy_id)
	return render_template('profile.html',user=user,vs=vec_sel,vb=vec_buy,title='Account Details')


@app.route('/profile/update', methods=["POST","GET"])
@login_required
def profile_update():
	form=updateUserForm()
	user=User.query.get_or_404(current_user.id)
	if form.validate_on_submit():
		current_user.Username=form.Username.data
		current_user.Email=form.Email.data
		current_user.Address=form.Address.data
		current_user.phone=form.Phno.data
		flash("your profile details are Updated")
		return redirect(url_for("home"))
	elif request.method=='GET':
		form.Username.data=current_user.Username
		form.Email.data=current_user.Email
		form.Address.data=current_user.Address
		form.Phno.data=current_user.phone
	return render_template("update_user.html",form=form)




