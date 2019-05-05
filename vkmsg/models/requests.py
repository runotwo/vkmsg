import requests


class IncomingMessage(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            if key == 'attachments':
                self.attachments = [Attachment(**x) for x in kwargs[key]]
                continue
            setattr(self, key, kwargs[key])


class IncomingRequest(object):
    def __init__(self, type, group_id, **kwargs):
        self.type = type
        self.group_id = group_id
        dialog_messages = ['message_new', 'message_reply', 'message_edit']
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if self.type in dialog_messages:
            self.object = IncomingMessage(**self.object)


class Attachment(object):
    def __init__(self, type, **kwargs):
        self.type = type
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if self.type == 'photo':
            self.photo = Photo(**self.photo)


class Photo(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            if key == 'sizes':
                self.image_url = kwargs[key][-1]['url']
                continue
            setattr(self, key, kwargs[key])

    def get_image(self):
        return requests.get(self.image_url).content
