import pytest

from vkmsg.models.keyboards import Keyboard, Button


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

