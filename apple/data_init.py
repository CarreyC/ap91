from apple import db
from apple.trade.models import Category

def category_data():
	has_data = Category.query.all()
	if has_data:
		return
		
	datas = [
			['MacBook', '蘋果筆記型電腦'],
			['iPhone', '蘋果手機'],
			['iPad', '蘋果平板'],
			['iMac', '蘋果桌上型電腦'],
			['Apple Watch', '蘋果手錶'],
			['Apple Pencil', '蘋果手寫筆'],
			['Magic Mouse', '蘋果滑鼠'],
			['Apple TV', '蘋果電視盒']
			]
	for data in datas:
		item = Category(name=data[0], desc=data[1])
		db.session.add(item)

	db.session.commit()