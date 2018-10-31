import json

import requests

from .helpers import get_query_string
from .errors import VkError


class VkClient(object):
    def __init__(self, token, group_id):
        self.token = token
        self.group_id = group_id
        self._vk_api_url = 'https://api.vk.com/method'
        self._api_version = '5.87'

    def set_webhook(self, url: str, title: str):
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if not isinstance(title, str):
            raise TypeError('title must be an instance of str')
        result = self.post_request('groups.addCallbackServer', {'url': url, 'title': title})
        if 'error' in result:
            raise VkError(**result['error'])
        return result

    def post_request(self, endpoint: str, data: dict):
        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be an instance of str')
        if not isinstance(data, dict):
            raise TypeError('data must be an instance of dict')
        headers = requests.utils.default_headers()
        query_string = get_query_string(access_token=self.token, v=self._api_version, group_id=self.group_id, **data)
        response = requests.post(f'{self._vk_api_url}/{endpoint}' + query_string, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)
