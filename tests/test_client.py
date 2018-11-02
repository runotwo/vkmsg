import pytest
import requests_mock

from vkmsg import VkClient
from vkmsg.models.keyboards import Keyboard, Button
from vkmsg.models.messages import Message


@requests_mock.Mocker(kw='mock')
class TestClient:
    _vk_api_url = 'https://api.vk.com/method'

    def test_Client(self, **kw):
        mock = kw['mock']
        mock.register_uri('POST', self._vk_api_url + '/groups.getCallbackConfirmationCode',
                          json={'response': {'code': '123'}})
        mock.register_uri('POST', self._vk_api_url + '/messages.send',
                          json={'response': {'code': '123'}})
        c = VkClient('123', 123)

        with pytest.raises(AttributeError):
            c.process_json({'type': 'message_new',
                            'object': {'date': 1541166755, 'from_id': 94833915, 'id': 9, 'out': 0, 'peer_id': 94833915,
                                       'text': 'hello', 'conversation_message_id': 3, 'fwd_messages': [],
                                       'important': False, 'random_id': 0, 'attachments': [],
                                       'payload': '{"hello":"hello"}', 'is_hidden': False}, 'group_id': 173320666})
        with pytest.raises(AttributeError):
            c.process_json({'type': 'message_new',
                            'object': {'date': 1541166858, 'from_id': 94833915, 'id': 11, 'out': 0, 'peer_id': 94833915,
                                       'text': 'Привет', 'conversation_message_id': 5, 'fwd_messages': [],
                                       'important': False, 'random_id': 0, 'attachments': [], 'is_hidden': False},
                            'group_id': 173320666})
        with pytest.raises(Exception):
            c.process_json({'type': 'qqq',
                            'object': {'date': 1541166858, 'from_id': 94833915, 'id': 11, 'out': 0, 'peer_id': 94833915,
                                       'text': 'Привет', 'conversation_message_id': 5, 'fwd_messages': [],
                                       'important': False, 'random_id': 0, 'attachments': [], 'is_hidden': False},
                            'group_id': 173320666})
        b = Button('', '', '')
        k = Keyboard([[b]])
        m = Message('hello', k)
        c.send_message(123, m)
        with pytest.raises(TypeError):
            c.send_message('', m)
        with pytest.raises(TypeError):
            c.send_message(123, '')

        @c.register_text_message_processor()
        def f(request):
            pass

        @c.register_callback_processor()
        def f(request):
            pass

        c.process_json({'type': 'message_new',
                        'object': {'date': 1541166755, 'from_id': 94833915, 'id': 9, 'out': 0, 'peer_id': 94833915,
                                   'text': 'hello', 'conversation_message_id': 3, 'fwd_messages': [],
                                   'important': False, 'random_id': 0, 'attachments': [],
                                   'payload': '{"hello":"hello"}', 'is_hidden': False}, 'group_id': 173320666})

        c.process_json({'type': 'message_new',
                        'object': {'date': 1541166858, 'from_id': 94833915, 'id': 11, 'out': 0, 'peer_id': 94833915,
                                   'text': 'Привет', 'conversation_message_id': 5, 'fwd_messages': [],
                                   'important': False,
                                   'random_id': 0, 'attachments': [], 'is_hidden': False}, 'group_id': 173320666})
