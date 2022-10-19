from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import create_card, delete_card, get_all_cards, increment_complete_card

from todo_app.flask_config import Config
from todo_app.models.ViewModel import ViewModel

def create_app():
        
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items_to_display = get_all_cards()

        view_model = ViewModel(items_to_display)
        
        return render_template('index.html', view_model=view_model)

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
    
    return app
