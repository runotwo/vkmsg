class Button(object):
    def __init__(self, label: str, payload: str, color: str = "Primary"):
        if not isinstance(label, str):
            raise TypeError('label must be an instance of str')
        if not isinstance(payload, str):
            raise TypeError('payload must be an instance of str')
        if not isinstance(color, str):
            raise TypeError('color must be an instance of str')
        self.label = label
        self.payload = payload
        self.color = color

    def to_dict(self):
        return {
            'action': {
                'type': 'text',
                'label': self.label,
                'payload': self.payload
            },
            'color': self.color
        }


class Keyboard(object):
    def __init__(self, button_rows: list, one_time: bool = False):
        for row in button_rows:
            if not isinstance(row, list):
                raise TypeError('row must be an instance of list')
            for button in row:
                if not isinstance(button, Button):
                    raise TypeError('button must be an instance of Button')
        if not isinstance(one_time, bool):
            raise TypeError('one_time must be an instance of bool')
        self.button_rows = button_rows
        self.one_time = one_time

    def to_dict(self):
        return {
            'one_time': self.one_time,
            "buttons": [[button.to_dict() for button in row] for row in self.button_rows]
        }
