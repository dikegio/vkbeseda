from flask import Flask, request, json

import vk_api
import random

vk = vk_api.VkApi(token=c789048fbd4fcddcdb1bff75070d4d3cb5d3f1a545f85ef08493bb977b1f7d69ca0c0060c9845d6fcf2fa)

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def main():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return "код подтверждения"
    elif data["type"] == "message_new":
        object = data["object"]
        id = object["peer_id"]
        body = object["text"]
        if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 200288454)})
        elif body.lower() == "я не подписан на канал it things":
                vk.method("messages.send", {"peer_id": id, "message": "Казнить грешника!", "random_id": random.randint(1, 200288454)})
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Не понял тебя!", "random_id": random.randint(1, 200288454)})
    return "ok"
