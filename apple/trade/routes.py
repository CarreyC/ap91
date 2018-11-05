from flask import Blueprint, render_template
from apple.trade.models import Banner

trade = Blueprint('trade', __name__)

@trade.route('/')
def start():
	banners = Banner.query.all()
	return render_template('index.html', banners=banners)

@trade.route('/alter')
def alter():
	return render_template('index_alternative.html')

@trade.route('/page_full')
def page_full():
	return render_template('page_full.html')

@trade.route('/page_left')
def page_left():
	return  render_template('page_sidebar_left.html')

@trade.route('/page_right')
def page_right():
	return  render_template('page_sidebar_right.html')

@trade.route('/portfolio_4')
def portfolio_4():
	return  render_template('portfolio_4column.html')

@trade.route('/portfolio_2')
def portfolio_2():
	return  render_template('portfolio_2column.html')

@trade.route('/portfolio_1')
def portfolio_1():
	return  render_template('portfolio_1column.html')

@trade.route('/portfolio_s')
def portfolio_s():
	return  render_template('portfolio_single.html')

@trade.route('/blog_overview')
def blog_overview():
	return  render_template('blog_overview.html')

@trade.route('/blog_single')
def blog_single():
	return  render_template('blog_single.html')

@trade.route('/contact')
def contact():
	return  render_template('contact.html')





