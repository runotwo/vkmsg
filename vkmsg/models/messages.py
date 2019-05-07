from .keyboards import Keyboard


class Attachment(object):
    def __init__(self, type, owner_id, media_id):
        self.type = type
        self.owner_id = owner_id
        self.media_id = media_id

    def to_str(self):
        return f'{self.type}{self.owner_id}_{self.media_id}'


class Message(object):
    def __init__(self, message: str, keyboard: Keyboard = None, attachments=None):
        if not isinstance(message, str):
            raise TypeError('message must be an instance of str')
        if keyboard is not None:
            if not isinstance(keyboard, Keyboard):
                raise TypeError('keyboard must be an instance of Keyboard')
        self.message = message
        self.keyboard = keyboard
        self.attachments = attachments

    def to_dict(self):
        res = {
            'message': self.message,
        }
        if self.keyboard:
            res['keyboard'] = self.keyboard.to_dict()
        if self.attachments:
            res['attachment'] = ','.join([x.to_str() for x in self.attachments])
        return res
