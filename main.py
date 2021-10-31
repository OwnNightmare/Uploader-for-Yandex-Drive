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
            return f'{self.name} is more intelligent than {other.name}'

    def __lt__(self, other):
        if self.intellect < other.intellect:
            return f'{self.name} is less intelligent than {other.name}'

    def __eq__(self, other):
        if self.intellect == other.intellect:
            return f'{self.name} and {other.name} are equal by intelligence'

    def __str__(self):
        return self.name

    def show_hero_js(self):
        pprint(self.hero_js)

    def show_hero_id(self):
        hero_id = self.hero_js['results'][0]['id']
        return hero_id


def find_smartest(given_heroes):
    smartest = ''
    heroes = []
    points = 0
    for hero in given_heroes:
        if isinstance(hero, Hero):
            heroes.append(hero)
        else:
            return f'{hero.name} is not Hero type'
    for hero in heroes:
        if hero.intellect >= points:
            points = hero.intellect
            smartest = hero.name
    if smartest is not False:
        return f'The most intelligence hero is {smartest} - {points} points'


def rate_heroes_by_intellect(heroes):
    place = 1
    summoned_heroes = []
    for hero in heroes:
        if isinstance(hero, Hero):
            summoned_heroes.append(hero)
        elif isinstance(hero, list):
            for character in hero:
                if isinstance(character, Hero):
                    summoned_heroes.append(character)
    print('\t Heroes by intelligence:'.upper())
    for hero in sorted(summoned_heroes, key=lambda x: x.intellect, reverse=True):
        print(f'{place}.{hero.name} - {hero.intellect} points')
        place += 1


def launch_heroes():
    Hulk = Hero('Hulk')
    Harry = Hero('Harry Potter')
    Thanos = Hero('Thanos')
    Captain = Hero('Captain America')
    Venom = Hero('Venom')
    Batman = Hero('Batman')
    Sauron = Hero('Sauron')
    Yoda = Hero('Yoda')
    Naruto = Hero('Naruto Uzumaki')
    Strange = Hero('Doctor Strange')
    Octopus = Hero('Doctor Octopus')
    my_heroes = [Hulk, Thanos, Captain, Harry, Venom, Batman, Sauron, Yoda, Naruto]
    others = (Strange, Octopus)
    AntMan = Hero('Ant-Man')
    print(find_smartest(my_heroes))
    rate_heroes_by_intellect([my_heroes, others, AntMan])


if __name__ == '__main__':
    launch_heroes()
