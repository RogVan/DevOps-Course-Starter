from datetime import datetime

class Item:
    def __init__(self, id: str, name: str, was_changed_today: bool, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status
        self.was_changed_today = was_changed_today

    @classmethod
    def from_trello_card(self, card, list):
        date_today = datetime.today().date()
        date_of_last_activity = datetime.strptime(card['dateLastActivity'].split('T')[0], '%Y-%m-%d').date()

        was_changed_today = date_today == date_of_last_activity

        return self(card['id'], card['name'], was_changed_today, list['name'])
