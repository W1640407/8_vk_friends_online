import getpass

import vk

APP_ID = 6222335


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline()
    return api.users.get(user_ids=friend_ids)


def output_friends_to_console(friends_online):
    print('You have {} friends online:'.format(len(friends_online)))
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = input('Enter VK Login: ')
    password = getpass.getpass(prompt='Enter VK password: ')
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
