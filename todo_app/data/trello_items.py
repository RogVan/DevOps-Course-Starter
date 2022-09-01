import os
from requests import get, put, delete, post

from todo_app.models.Item import Item

BOARD_ID = os.getenv('TRELLO_BOARD_ID')
TO_DO_LIST_ID = os.getenv('TRELLO_TO_DO_LIST_ID')
IN_PROGRESS_LIST_ID = os.getenv('TRELLO_IN_PROGRESS_LIST_ID')
COMPLETED_LIST_ID = os.getenv('TRELLO_COMPLETED_LIST_ID')

KEY = os.getenv('TRELLO_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')

def delete_card(cardId):
    headers = {"Accept": "application/json"}

    query = {'key': KEY, 'token': TOKEN}

    delete(
        f'https://api.trello.com/1/cards/{cardId}',
        headers=headers,
        params=query
        )
    
def create_card(title):
    headers = {"Accept": "application/json"}

    query = {
    'idList': TO_DO_LIST_ID,
    'name' : title,
    'key': KEY,
    'token': TOKEN
    }

    post(
    "https://api.trello.com/1/cards",
    headers=headers,
    params=query
    )

def increment_complete_card(cardId):
    card_to_move:Item = [card for card in get_all_cards() if card.id == cardId][0]

    print(card_to_move.status)

    if card_to_move.status == 'In Progress':
        put(f'https://api.trello.com/1/cards/{cardId}/?idList={COMPLETED_LIST_ID}&key={KEY}&token={TOKEN}')
    elif card_to_move.status  == 'To Do':
        put(f'https://api.trello.com/1/cards/{cardId}/?idList={IN_PROGRESS_LIST_ID}&key={KEY}&token={TOKEN}')


def get_all_cards():
    all_cards = []
    board = get(f'https://api.trello.com/1/boards/{BOARD_ID}/lists?cards=open&key={KEY}&token={TOKEN}').json()

    for list in board:
        list_cards = [Item.from_trello_card(card, list) for card in list['cards'] ]
        all_cards+=list_cards

    return sorted(all_cards, key=lambda item: item.status, reverse=True)

    
