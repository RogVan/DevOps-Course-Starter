from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, delete_item, get_item, get_items, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    itemsToDisplay = sorted(get_items(), key=lambda item: item['status'], reverse=True)

    return render_template('index.html', items=itemsToDisplay)

@app.route('/add', methods=['POST'])
def addNewItem():
    newItemTitle = request.form['addItemFormTitle']
    add_item(newItemTitle)

    return redirect('/')

@app.route('/mark-complete/<itemId>')
def markItemComplete(itemId):
    itemToUpdate = get_item(int(itemId))
    itemToUpdate['status'] = 'Complete'
    save_item(itemToUpdate)

    return redirect('/')

@app.route('/delete/<itemId>')
def deleteItem(itemId):
    delete_item(int(itemId))

    return redirect('/')
    
