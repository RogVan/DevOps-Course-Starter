import os
from requests import get, put, delete, post

from todo_app.models.Item import Item

BOARD_ID = os.getenv('TRELLO_BOARD_ID')
TO_DO_LIST_ID = os.getenv('TRELLO_TO_DO_LIST_ID')
IN_PROGRESS_LIST_ID = os.getenv('TRELLO_IN_PROGRESS_LIST_ID')
COMPLETED_LIST_ID = os.getenv('TRELLO_COMPLETED_LIST_ID')

key = os.getenv('TRELLO_KEY')
token = os.getenv('TRELLO_TOKEN')

def delete_card(cardId):
    headers = {"Accept": "application/json"}

    query = {'key': key, 'token': token}

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
    'key': key,
    'token': token
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
        put(f'https://api.trello.com/1/cards/{cardId}/?idList={COMPLETED_LIST_ID}&key={key}&token={token}')
    elif card_to_move.status  == 'To Do':
        put(f'https://api.trello.com/1/cards/{cardId}/?idList={IN_PROGRESS_LIST_ID}&key={key}&token={token}')


def get_all_cards():
    all_cards = []
    board = get(f'https://api.trello.com/1/boards/{BOARD_ID}/lists?cards=open&key={key}&token={token}').json()

    for list in board:
        list_cards = [Item.from_trello_card(card, list) for card in list['cards'] ]
        all_cards+=list_cards

    return sorted(all_cards, key=lambda item: item.status, reverse=True)

    
