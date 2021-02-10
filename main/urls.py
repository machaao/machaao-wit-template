from main import app, wit, machaao
from flask import request, Response
import os, json
from .helper import custom_request_handler, get_trait, get_chatbot_response

@app.route('/machaao/incoming', methods=["POST"])
def index():
    incoming_data = custom_request_handler(request)

    user_id = incoming_data["user_id"]
    message = incoming_data["messaging"]
    message = message[0]["message_data"]["text"]

    processed_message = wit.message(message)

    trait = get_trait(processed_message)

    chatbot_response = get_chatbot_response(trait)

    payload = {
        "identifier": "BROADCAST_FB_QUICK_REPLIES",
        "users": [user_id],
        "message": {"text": chatbot_response},
    }

    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py

    response = machaao.send_message(payload)

    return Response(
        mimetype="application/json",
        response=json.dumps({ "success": True, "message": response.text }),
        status=200,
    )
