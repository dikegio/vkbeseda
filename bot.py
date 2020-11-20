from flask import Flask, request, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import vk_api
import random

vk = vk_api.VkApi(token=token)

app = Flask(__name__)

longpoll = VkBotLongPoll(vk, "200288454")

print("Бот запущен")

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": event.object.text,
                                                "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                "random_id": 0})
