#!/usr/bin/env python3

'''''''''''''''''''''''''''''
COPYRIGHT FETCH DEVELOPMENT,
2020
ALL RIGHTS RESERVED
'''''''''''''''''''''''''''''

#CHANGEABLE AREA
KEYWORDS = ["1", "2", "3"]
ANSWERS =  ["one", "two", "three"]

#DEVELOPMENT AREA, DO NOT CHANGE
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

def get_random_id():
	return random.getrandbits(31) * random.choice([-1, 1])
def write_msg(user_id, message):
	operator.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})

token = "a567f5ca8bb9d4a6c4240102e7670055fff3941098e03a8204858489cb80a7f27e29e1a5f05fe270ef975"
operator = vk_api.VkApi(token=token)
longpoll = VkLongPoll(operator)

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text
		for i in range(0, len(KEYWORDS)):
			if text == KEYWORDS[i]:
				write_msg(event.user_id, ANSWERS[i])
