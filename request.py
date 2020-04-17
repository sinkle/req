import requests
import constants
import datetime


def calc_age():
    pass


def get_user_id(user_ids):
    payload = {
        'v': 5.71,
        'access_token': constants.ACCESS_TOKEN,
        "user_ids": user_ids,
    }
    response = requests.get('https://api.vk.com/method/users.get', params=payload)
    return response


def get_friends(user_id):
    payload = {
        'v': 5.71,
        'access_token': constants.ACCESS_TOKEN,
        "user_id": user_id,
        "fields": "bdate"
    }
    return requests.get('https://api.vk.com/method/friends.get', params=payload)




id = get_user_id("id254466147").json()['response'][0]['id']
list_of_friends = get_friends(id)
print(list_of_friends.url)
print(list_of_friends.text)
print()
for i in list_of_friends.json()['response']['items']:
    try:
        print(i['bdate'], i['first_name'], i['last_name'] )
    except KeyError:
        print('No data')
