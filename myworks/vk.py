from email import message
import vk_api
token = 'vk1.a.GFHFGHF-t-TfwNEReYmzccdf8-99RByGrwc6nWnsVl6ACeMV2pTxtEw1N-elJXYPl-a64NrqeeW9fjDA6GoM7Fup1N6jzImTkm2Wyrk1dA1WyKWMI83i3D94lbPQaweUfTanvpJOGUUC7iF2RZSVZ_r3nia'
session = vk_api.VkApi(token=token)
vk = session.get_api()
my_id = 56456464
zhenya_id = 45646
alina_id = 5645


action = input('Что делаем?\n')
if action == 'пишем смс':
    person = input('Кому пишем?))\n')
    if person == 'Алина':
        msg = input('')
        vk.messages.send(user_id=alina_id, message=msg, random_id=0)
    elif person == 'Женя':
        msg = input('')
        vk.messages.send(user_id=zhenya_id, message=msg, random_id=0)
    else:
        print('такого человека нет у вас в друзьях')
else:
    msg = input('')
    vk.wall.post(owner_id=my_id, friends_only=0,
                 message=msg, status=0, long=180)
