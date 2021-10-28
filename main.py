import requests
from pprint import pprint


class Hero:
    url = 'https://superheroapi.com/api/2619421814940190/'

    def __init__(self, name):
        self.name = name
        resp = requests.get(Hero.url + f'search/{self.name}')
        self.hero_js = resp.json()

    def show_hero_js(self):
        pprint (self.hero_js)

    def show_hero_id(self):
        hero_id = self.hero_js['results'][0]['id']
        return hero_id


def find_smartest(given_heroes):
    smartest= ''
    heroes = []
    points = 0
    for hero in given_heroes:
        if isinstance(hero, Hero):
            heroes.append(hero)
        else:
            return f'{hero.name} is not Hero type'
    for hero in heroes:
        if int(hero.hero_js['results'][0]['powerstats']['intelligence']) >= points:
            points = int(hero.hero_js['results'][0]['powerstats']['intelligence'])
            smartest = hero.name
    if smartest is not False:
        return f'The most intelligence hero is {smartest} - {points} points'

# Hulk = 'search/Hulk'
# Captain = 'search/Captain America'
# Thanos = 'search/Thanos'
# response = requests.get(url + Thanos)
# pprint(response.json()['results'][0]['id'])
# # print(response.json()['results'][0]['powerstats']['intelligence'])

hulk = Hero('Hulk')
Thanos = Hero('Thanos')

print(find_smartest([hulk, Thanos]))
# hulk.show_hero_js()








# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
