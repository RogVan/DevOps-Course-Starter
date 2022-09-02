from todo_app.models.Item import Item
from todo_app.models.ViewModel import ViewModel

items_1 = [
    Item('1', 'not yet started item', True, 'To Do'),
    Item('2', 'in progress item', True, 'In Progress'),
    Item('3', 'completed today item', True, 'Complete'),
    Item('4', 'completed yesterday item', False, 'Complete')
]

items_2 = [
    Item('1', 'not yet started item', True, 'To Do'),
    Item('2', 'in progress item', True, 'In Progress'),
    Item('3', 'completed today item', True, 'Complete'),
    Item('4', 'completed today item', True, 'Complete'),
    Item('5', 'completed today item', True, 'Complete'),
    Item('6', 'completed today item', True, 'Complete'),
    Item('7', 'completed today item', True, 'Complete'),
    Item('8', 'completed yesterday item', False, 'Complete')
]

def test_gets_in_progress_items():
    '''Only returns items in progress'''

    view_model = ViewModel(items_1)

    result = view_model.in_progress_items

    assert(len(result)) == 1
    assert(result[0].name) == 'in progress item'

def test_gets_all_completed_items():
    '''Returns all completed items if fewer than 5'''

    view_model = ViewModel(items_1)

    result = view_model.completed_items

    assert(len(result['display_by_default'])) == 2
    assert(len(result['expand_to_display'])) == 0

def test_gets_todays_completed_items():
    '''Returns items completed today by default if more than 5'''

    view_model = ViewModel(items_2)

    result = view_model.completed_items

    assert(len(result['display_by_default'])) == 5
    assert(len(result['expand_to_display'])) == 1
    

def test_gets_not_started_items():
    '''Only returns not started items'''

    view_model = ViewModel(items_1)

    result = view_model.to_do_items

    assert(len(result)) == 1
    assert(result[0].name) == 'not yet started item'
