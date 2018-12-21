from flask import Flask, request
from vkmsg import VkClient, messages

app = Flask(__name__)
client = VkClient('<YOUR_TOKEN>', '<YOUR_GROUP_ID>')


@client.register_text_message_processor()
def text_handler(incoming):
    msg = messages.Message(incoming.object.text)
    client.send_message(incoming.object.from_id, msg)


@app.route('/incoming')
def incoming():
    if request.json:
        client.process_json(request.json)
    return ''
