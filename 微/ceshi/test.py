from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter
from pp import main
from config import session,Article
app = Flask(__name__)




@app.route('/')
def index():
	PER_PAGE = 5
	total = session.quer(Article).count()
	print(total)
	page = request.args.get(get_page_parameter(), type=int, default=1)
	print('45',page)
	print(type(page))
	start = (page - 1) * PER_PAGE
	end = start + PER_PAGE
	pagination = Pagination(bs_version=3, page=page, total=total)
	articles = session.quer(Article).slice(start, end)
	con = {
		'pagination': pagination,
		'articles': articles
	}
	return render_template('b.html', **con)

#def y():

if __name__ == '__main__':
	app.run(debug=True)
