import requests
import constants
import datetime


def dict_to_list_of_tuples(dictionary):
    l = []
    for key in dictionary:
        l.append((key, dictionary[key]))
    return l


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


def how_old(str_bdate):
    curr_year, curr_month, curr_day = str(datetime.date.today()).split('-')
    try:
        day_bdate, month_bdate, year_bdate = str_bdate.split('.')
    except ValueError:
        return None
    if int(month_bdate) < int(curr_month):
        return int(curr_year) - int(year_bdate)
    elif int(month_bdate) > int(curr_month):
        return int(curr_year) - int(year_bdate) - 1
    elif int(curr_day) < int(day_bdate):
        return int(curr_year) - int(year_bdate) - 1
    else:
        return int(curr_year) - int(year_bdate)


def count_number_age(dict_age, age):
    try:
        dict_age[age] += 1
    except KeyError:
        dict_age[age] = 1
    return dict_age[age]


if __name__ == '__main__':
    data = input("Enter 'user_id' or 'username'\n")
    if not isinstance(data, int):
        user_id = get_user_id("obzzzen").json()['response'][0]['id']
    else:
        user_id = data
    list_of_friends = get_friends(user_id)
    dict_ages = {}
    for i in list_of_friends.json()['response']['items']:
        try:
            age = how_old(i['bdate'])
        except KeyError:
            continue
        if age is None:
            continue
        count_number_age(dict_ages, age)
    res_without_sort = dict_to_list_of_tuples(dict_ages)
    res = sorted(res_without_sort, key=lambda tup: tup[0], reverse=True)
    print(res)
