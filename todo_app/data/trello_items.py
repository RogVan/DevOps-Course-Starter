import os
import requests

from todo_app.models.Item import Item

def delete_card(cardId):
    KEY = os.getenv('TRELLO_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    headers = {"Accept": "application/json"}

    query = {'key': KEY, 'token': TOKEN}

    requests.delete(
        f'https://api.trello.com/1/cards/{cardId}',
        headers=headers,
        params=query
        )
    
def create_card(title):
    KEY = os.getenv('TRELLO_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    TO_DO_LIST_ID = os.getenv('TRELLO_TO_DO_LIST_ID')

    headers = {"Accept": "application/json"}

    query = {
    'idList': TO_DO_LIST_ID,
    'name' : title,
    'key': KEY,
    'token': TOKEN
    }

    requests.post(
    "https://api.trello.com/1/cards",
    headers=headers,
    params=query
    )

def increment_complete_card(cardId):
    KEY = os.getenv('TRELLO_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    IN_PROGRESS_LIST_ID = os.getenv('TRELLO_IN_PROGRESS_LIST_ID')
    COMPLETED_LIST_ID = os.getenv('TRELLO_COMPLETED_LIST_ID')
    card_to_move:Item = [card for card in get_all_cards() if card.id == cardId][0]

    print(card_to_move.status)

    if card_to_move.status == 'In Progress':
        requests.put(f'https://api.trello.com/1/cards/{cardId}/?idList={COMPLETED_LIST_ID}&key={KEY}&token={TOKEN}')
    elif card_to_move.status  == 'To Do':
        requests.put(f'https://api.trello.com/1/cards/{cardId}/?idList={IN_PROGRESS_LIST_ID}&key={KEY}&token={TOKEN}')


def get_all_cards():
    KEY = os.getenv('TRELLO_KEY')
    TOKEN = os.getenv('TRELLO_TOKEN')
    BOARD_ID = os.getenv('TRELLO_BOARD_ID')
    all_cards = []
    board = requests.get(f'https://api.trello.com/1/boards/{BOARD_ID}/lists?cards=open&key={KEY}&token={TOKEN}').json()

    for list in board:
        list_cards = [Item.from_trello_card(card, list) for card in list['cards'] ]
        all_cards+=list_cards

    return sorted(all_cards, key=lambda item: item.status, reverse=True)

    
