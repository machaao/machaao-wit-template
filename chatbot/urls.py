from chatbot import app, wit
from flask import request, Response
from machaao import request_handler, send_message
import os

MESSENGERX_API_TOKEN = os.environ['MESSENGERX_API_TOKEN']
MESSENGERX_BASE_URL = os.environ['MESSENGERX_BASE_URL']

@app.route('/machaao/incoming', methods=["POST"])
def index():
    incoming_data = request_handler(request)

    user_id = incoming_data["user_id"]
    message = incoming_data["messaging"]
    message = message[0]["message_data"]["text"]

    processed_message = wit.message(message)
    # Do Something with processed message.

    payload = {
        "identifier": "BROADCAST_FB_QUICK_REPLIES",
        "users": [user_id],
        "message": {"text": message},
    }

    print(f"sending message -> using token: {MESSENGERX_API_TOKEN}, base_url: {MESSENGERX_BASE_URL}")


    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py
    response = send_message(MESSENGERX_API_TOKEN, MESSENGERX_BASE_URL, payload)

    output_payload = {
        "success": True,
        "message": response.text,
    }

    return Response(
        mimetype="application/json",
        response=json.dumps(output_payload),
        status=200,
    )