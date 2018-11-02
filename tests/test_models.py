import pytest

from vkmsg.errors import VkError
from vkmsg.models.keyboards import Keyboard, Button
from vkmsg.models.messages import Message
from vkmsg.models.requests import IncomingMessage, IncomingRequest


class TestKeyboards:
    def test_Button(self):
        b = Button('', '', '')
        assert b.to_dict() == {'action': {
            'type': 'text',
            'label': '',
            'payload': ''
        },
            'color': ''
        }
        with pytest.raises(TypeError):
            Button(1, '', '')
        with pytest.raises(TypeError):
            Button('', 1, '')
        with pytest.raises(TypeError):
            Button('', '', 1)

    def test_Keyboard(self):
        b = Button('', '', '')
        k = Keyboard([[b]])
        assert k.to_dict() == {
            'one_time': False,
            "buttons": [[{'action': {
                'type': 'text',
                'label': '',
                'payload': ''
            },
                'color': ''
            }]]
        }
        k.row([b])
        with pytest.raises(TypeError):
            Keyboard([[b]], '')
        with pytest.raises(TypeError):
            Keyboard([['']])
        with pytest.raises(TypeError):
            Keyboard([b], False)
        with pytest.raises(TypeError):
            Keyboard(1)
        with pytest.raises(TypeError):
            k.row(1)
        with pytest.raises(TypeError):
            k.row([1])


class TestMessages:
    def test_Message(self):
        b = Button('', '', '')
        k = Keyboard([[b]])
        m = Message('hello', k)
        assert m.to_dict() == {
            'message': 'hello',
            'keyboard': {
                'one_time': False,
                "buttons": [[{'action': {
                    'type': 'text',
                    'label': '',
                    'payload': ''
                },
                    'color': ''
                }]]
            }
        }
        with pytest.raises(TypeError):
            Message(1, k)
        with pytest.raises(TypeError):
            Message('hello', 1)


class TestRequests:
    def test_IncomingMessage(self):
        IncomingMessage(**{'test': 'test'})

    def test_IncomingTestMessage(self):
        IncomingRequest('message_new', '', **{'object': {'test': 'test'}})


class TestHelpers:
    def test_helpers(self):
        assert str(VkError(100, 'test', {})) == 'CODE: 100 MSG: test'
