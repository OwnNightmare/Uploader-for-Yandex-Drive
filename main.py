import requests
from pprint import pprint


class Hero:
    def __init__(self, name):
        self.name = name
        resp = requests.get(url + f'search/{self.name}')
        self.hero_js = resp.json()

    def show_hero_js(self):
        pprint (self.hero_js)

    def show_hero_id(self):
        hero_id = self.hero_js['results'][0]['id']
        return hero_id

    def most_intelligence(self, heroes):
        if type(heroes) == list:
            ...






url = 'https://superheroapi.com/api/2619421814940190/'
# Hulk = 'search/Hulk'
# Captain = 'search/Captain America'
# Thanos = 'search/Thanos'
# response = requests.get(url + Thanos)
# pprint(response.json()['results'][0]['id'])
# # print(response.json()['results'][0]['powerstats']['intelligence'])

hulk = Hero('Hulk')
hulk.show_hero_js()








# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
