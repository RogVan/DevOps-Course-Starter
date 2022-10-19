class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def in_progress_items(self):
        return [item for item in self.items if item.status == 'In Progress']

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == 'To Do']

    @property
    def completed_items(self):

        all_completed = [item for item in self.items if item.status =='Complete']

        display_by_default = [item for item in all_completed if item.was_changed_today == True]
        expand_to_display = [item for item in all_completed if item.was_changed_today == False]

        if len(all_completed) <= 5:
            return {'display_by_default': all_completed, 'expand_to_display': [], 'completed_text_label': 'Complete'}
        else:
            return {'display_by_default': display_by_default, 'expand_to_display': expand_to_display, 'completed_text_label': 'Completed Today'}
        
    