from apple import create_app
from apple.data_init import category_data

app = create_app()

with app.app_context():
	category_data() # 初始化分類資料

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)