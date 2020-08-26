import vk_api
import requests

session = requests.Session()

login, password = '89997307779', '12345'

vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth(token_only=True)

except vk_api.AuthError as error_msg:
    print(error_msg)
    #return


from vk_api.longpoll import VkLongPoll, VkEventType
long = 0
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную # фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Ваш текст'
		)
