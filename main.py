import requests
from pprint import pprint


class Hero:
    url = 'https://superheroapi.com/api/2619421814940190/'

    def __init__(self, name):
        self.name = name
        resp = requests.get(Hero.url + f'search/{self.name}')
        self.hero_js = resp.json()
        self.intellect = int(self.hero_js['results'][0]['powerstats']['intelligence'])

    def __gt__(self, other):
        if self.intellect > other.intellect:
            return True

    def __lt__(self, other):
        if self.intellect < other.intellect:
            return False

    def __eq__(self, other):
        if self.intellect == other.intellect:
            return True

    def __str__(self):
        return self.name

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


def rate_heroes_by_intellect(heroes):
    place = 1
    print('\t Heroes by intelligence:'.upper())
    for hero in sorted(heroes, key=lambda supe: supe.intellect, reverse=True ):
        print(f'{place}.{hero.name} - {hero.intellect} points')
        place += 1


Hulk = Hero('Hulk')
harry = Hero('Harry Potter')
Thanos = Hero('Thanos')
Captain = Hero('Captain America')
my_heroes = [Hulk, Thanos, Captain, harry]

print(find_smartest(my_heroes))
rate_heroes_by_intellect(my_heroes)





# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
