import random
import flask
from flask import request
from py import gs
import db

app = flask.Flask(__name__)
app.secret_key = 'qweasdzxcrtyuiofghjkvbnl;1237895425-09=90/*-+'


@app.route('/', methods=['GET', 'POST'])
def index():
	return flask.render_template('index.html', tou=db.sql_query(), f=db.sql_query_wz(), sc=db.sql_query_sc())


@app.route('/admin/')
def admin():
	if 'email' in flask.session:
		# print(db.sql_query_wz())
		return flask.render_template('admin/admin_admin.html', f=db.sql_query_wz())
	return flask.redirect(flask.url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
	if flask.request.method == 'GET':
		return flask.render_template('login.html')
	if flask.request.method == 'POST':
		mail = flask.request.form['email']
		password = flask.request.form['password']
		print(mail, password)
		op = db.sql_query_login()
		if mail == op[0] and password == op[1]:
			flask.session['email'] = flask.request.form['email'], flask.request.form['password']
			return flask.redirect(flask.url_for('admin'))
		return flask.redirect(flask.url_for('login'))
	return flask.redirect(flask.url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if flask.request.method == 'GET':
		return flask.render_template('register.html')
	if flask.request.method == 'POST':
		name = flask.request.form['name']
		passs = flask.request.form['passs']
		password = flask.request.form['password']
		if passs == password:
			db.sql_insert_register(name=name, password=passs)
			return flask.render_template('login.html')
		return flask.redirect(flask.url_for('register'))
	return flask.redirect(flask.url_for('register'))


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	print(flask.session)
	flask.session.pop('email', None)
	print(flask.session)
	return flask.redirect(flask.url_for('login'))


@app.route('/d', methods=['POST'])
def d():
	if len(request.form) == 1 and '1':
		to = request.form.get('name')
		# print('1')
		print(request.form)
		db.sql_modify(to=to)
		return flask.redirect(flask.url_for('admin_u_admin', url='admin_admin'))
	elif len(request.form) == 2 and '2':
		# to = request.form.get('name')
		wzb = request.form.get('wzb')
		wzw = request.form.get('wzw')
		print(request.form.get('wzb'))
		print(request.form.get('wzw'))
		db.sql_insert_wzz(wzb=wzb, wzw=wzw)
		return flask.redirect(flask.url_for('admin_u_admin', url='admin_admin'))
	else:
		return '错误'


@app.route('/admin_u/')
def admin_u():
	return flask.render_template('y/admin.html')


@app.route('/admin_u/admin/<url>', methods=['POST', 'GET'])
def admin_u_admin(url):
	if url == 'admin_admin':
		return flask.render_template(f'admin/{url}.html', op='a123456')
	elif url == 'admin_zy':
		return flask.render_template(f'admin/{url}.html', )
	elif url == 'admin_wz':
		return flask.render_template(f'admin/{url}.html', f=db.sql_query_wz())
	elif url == 'admin_sz':
		return flask.render_template(f'admin/{url}.html', )
	elif url == 'admin_xx':
		g = db.sql_query_sp()
		sp = random.choice(g)[1]
		return flask.render_template(f'admin/{url}.html', sp='mp4/' + sp)
	elif url == 'admin_zy':
		return flask.render_template(f'admin/{url}.html', )


@app.route('/wz/<idd>', )
def wz(idd):
	return flask.render_template('y/wz.html', u=db.sql_query_wzz(idd), tou=db.sql_query_wzz(idd)[0][1])


@app.route('/se', methods=['POST'])
def se():
	if flask.request.form.get('sc') == 'sc':
		print(flask.request.form.get('sc'))
		o = gs.sc()
		return flask.render_template('admin/admin_sz.html', o=o, t=1)
	if flask.request.form.get('xs') == 'xs':
		oo = db.sql_query_sc()
		return flask.render_template('admin/admin_sz.html', o=oo, t=2)


@app.route('/sp', methods=['POST'])
def sp():
	if flask.request.form.get('sp') == 'sp':
		print(flask.request.form.get('sp'))
		g = db.sql_query_sp()
		spp = random.choice(g)[1]
		return flask.render_template('admin/admin_xx.html', sp='mp4/' + spp)


@app.errorhandler(404)
def f_404(error):
	return flask.render_template('404.html')


@app.errorhandler(405)
def f_405(error):
	return flask.render_template('405.html')


@app.errorhandler(500)
def f_500(error):
	return flask.render_template('500.html')


if __name__ == '__main__':
	app.run(port=4, debug=True, host='0.0.0.0')
