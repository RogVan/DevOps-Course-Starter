class Item:
    def __init__(self, id: str, name: str, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(self, card, list):
        return self(card['id'], card['name'], list['name'])
