from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

items = []
@main.route('/')
def index():
	return render_template('homepage.html', items=items)

@main.route('/list')
def list():
	return render_template('list.html', items=items)

@main.route('/remove', methods=['POST'])
def list_remove():
	list_remove = request.form.get('removes')
	if list_remove:
		items.remove(f'{list_remove}')
	return render_template('homepage.html', items=items)

@main.route('/list_post', methods=['POST'])
def list_post():
	list_item = request.form.get('items')
	if list_item:
		items.append(f'{list_item}')
	return render_template('homepage.html',items=items)

@main.route('/drop_down_remove', methods=['POST'])
def drop_down():
	list_remove = request.form.get('drop_down')
	if list_remove:
		items.remove(f'{list_remove}')
	return render_template('homepage.html', items=items)



#figure out why this requires a whole new page
"""@main.route('/remove')
def remove_page():
	return render_template('remove.html')
@main.route('/remove', methods=['POST'])
def list_remove():
	list_remove = request.form.get('removes')
	items.remove(f'{list_remove}')
	return render_template('homepage.html', items=items)"""


