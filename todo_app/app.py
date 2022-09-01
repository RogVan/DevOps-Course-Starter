from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import create_card, delete_card, get_all_cards, increment_complete_card

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    itemsToDisplay = get_all_cards()
    
    return render_template('index.html', items=itemsToDisplay)

@app.route('/add', methods=['POST'])
def addNewItem():
    newItemTitle = request.form['addItemFormTitle']

    if newItemTitle != '':
        create_card(newItemTitle)
        return redirect('/')
    
    return redirect('/')

@app.route('/mark-complete/<itemId>')
def markItemComplete(itemId):
    increment_complete_card(itemId)

    return redirect('/')

@app.route('/delete/<itemId>')
def deleteItem(itemId):
    delete_card(itemId)

    return redirect('/')
