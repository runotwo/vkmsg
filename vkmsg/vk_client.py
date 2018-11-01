import json

import requests

from .errors import VkError
from .helpers import get_query_string
from .models.messages import Message


class VkClient(object):
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self._vk_api_url = 'https://api.vk.com/method'
        self._api_version = '5.87'
        self.callback_confirmation_code = self.get_callback_confirmation_code()['code']

    def send_message(self, user_id: int, message: Message):
        if not isinstance(user_id, int):
            raise TypeError('user_id must be an instance of int')
        if not isinstance(message, Message):
            raise TypeError('message must be an instance of Message')
        msg = message.to_dict()
        msg['user_id'] = user_id
        result = self.post_request('messages.send', msg)
        if 'error' in result:
            raise VkError(**result['error'])
        return result['response']

    def get_callback_confirmation_code(self):
        result = self.post_request('groups.getCallbackConfirmationCode')
        if 'error' in result:
            raise VkError(**result['error '])
        return result['response']

    def set_webhook(self, url: str, title: str):
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if not isinstance(title, str):
            raise TypeError('title must be an instance of str')
        result = self.post_request('groups.addCallbackServer', {'url': url, 'title': title})
        if 'error' in result:
            raise VkError(**result['error'])
        return result['response']

    def post_request(self, endpoint: str, data: dict = None):
        if data is None:
            data = {}
        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be an instance of str')
        if not isinstance(data, dict):
            raise TypeError('data must be an instance of dict')
        headers = requests.utils.default_headers()
        query_string = get_query_string(access_token=self.token, v=self._api_version, group_id=self.group_id, **data)
        response = requests.post(f'{self._vk_api_url}/{endpoint}' + query_string, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)
