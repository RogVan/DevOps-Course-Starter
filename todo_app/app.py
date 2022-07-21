from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    itemsToDisplay = get_items()

    return render_template('index.html', items=itemsToDisplay)

@app.route('/add', methods=['POST'])
def addNewItem():
    newItemTitle = request.form['addItemFormTitle']
    add_item(newItemTitle)
    
    return redirect('/')
