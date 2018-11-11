from flask import Blueprint, render_template
from apple.trade.models import Banner, Category, CateSub
from apple.trade.utils import get_ctype

trade = Blueprint('trade', __name__)

@trade.route('/', methods=['GET'])
def start():
	banners = Banner.query.all()
	category = Category.query.all()
	return render_template('index.html', banners=banners, items=category)

@trade.route('/category/<ctype>', methods=['GET'])
def category(ctype):
	type_id = get_ctype(ctype)
	type_models = CateSub.query.filter_by(cate_main=type_id).all()
	print(len(type_models))
	return render_template('category.html', type_models=type_models)

@trade.route('/item_page')
def item_page():
	return render_template('item_page.html')










@trade.route('/cate')
def cate():
	return render_template('original/index_alternative.html')

@trade.route('/page_full')
def page_full():
	return render_template('original/page_full.html')

@trade.route('/page_left')
def page_left():
	return  render_template('original/page_sidebar_left.html')

@trade.route('/page_right')
def page_right():
	return  render_template('original/page_sidebar_right.html')

@trade.route('/portfolio_4')
def portfolio_4():
	return  render_template('original/portfolio_4column.html')

@trade.route('/portfolio_2')
def portfolio_2():
	return  render_template('original/portfolio_2column.html')

@trade.route('/portfolio_1')
def portfolio_1():
	return  render_template('original/portfolio_1column.html')

@trade.route('/portfolio_s')
def portfolio_s():
	return  render_template('original/portfolio_single.html')

@trade.route('/blog_overview')
def blog_overview():
	return  render_template('original/blog_overview.html')

@trade.route('/blog_single')
def blog_single():
	return  render_template('original/blog_single.html')

@trade.route('/contact')
def contact():
	return  render_template('original/contact.html')





