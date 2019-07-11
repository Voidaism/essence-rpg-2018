from random import randint
import time

class Rando:
    def rand(num):
        rand = randint(1, num)
        return rand

time.sleep(2)
print('...')
time.sleep(3.5)
print('Yet another one rises.')
time.sleep(3.5)
print('Welcome, forgotten one.')
time.sleep(2)
print('I am DYMINO. An AI programmed many centuries ago to protect the last of your kind, human.')
time.sleep(3.5)
print('Rendering history ...')
time.sleep(0.7)
print('... PROCESSING 33% ...')
time.sleep(0.5)
print('... PROCESSING 68% ...')
time.sleep(0.5)
print('... PROCESSING 100% ...')
time.sleep(3)
print(
    'In the year 2046, a war broke out, resulting in world collapsing into nuclear fallout. Some of mankind had been preserved in pods as a part of PROJECT FORGOTTEN. You were one such person. Many have others have risen before you and at this point in time humanity is reminiscent to those who existed in the 15th century. All kind of radiated organisms now roam the land so I prithee you be careful. Here, with the essence of these defeated Forgottens, I can imbue their abilities into you.')
time.sleep(7)
print('Now then, choose your essence. Templar / Bogatyr / Magus')


class CharClass:
    def __init__(self, name, hp, renown, bag=None, weapon=None):
        self.name = str(name)
        self.hp = int(hp)
        self.bag = bag
        self.renown = int(renown)
        self.weapon = str(weapon)


class Templar(CharClass):
    def __init__(self):
        super().__init__(name=input('Can you recall your name?'), weapon=input('What weapon do you use?'), hp=2000,
                         bag={'Hilt, armor, whiskey'}, renown=5)

    starter = 'Templar'
    maxhp = 2000


class Bogatyr(CharClass):
    def __init__(self):
        super().__init__(name=input('Can you recall your name?'), weapon=input('What weapon do you use?'), hp=1750,
                         bag={'Mace, saddle, flasks'}, renown=3)

    starter = 'Bogatyr'
    maxhp = 1750


class Magus(CharClass):
    def __init__(self):
        super().__init__(name=input('Can you recall your name?'), weapon=input('What is your talisman?'), hp=1500,
                         bag={'Bident, charms, chimes, staff'}, renown=3)

    starter = 'Magus'
    maxhp = 1600


class RampartGolem(CharClass):
    def __init__(self):
        super().__init__(name='Rampart Golem', hp=1200, bag={}, renown=8)


class Mutant(CharClass):
    def __init__(self):
        super().__init__(name='Mutant', hp=1000, bag={}, renown=3)


class Exile(CharClass):
    def __init__(self):
        super().__init__(name='Exile', hp=1150, bag={}, renown=7)


def essence():
    sessence = input('?')
    if sessence == 'Templar':
        print('You selected Templar as your starting class.')
        time.sleep(2)
        print(
            'You are an outcasted knight from the New Templar Order of poor renown who collapsed roaming the land. Sturdy, owing to high strength and stout armor.')
        champion = Templar()
        return champion
    elif sessence == 'Bogatyr':
        print('You selected Bogatyr as your starting class.')
        time.sleep(2)
        print(
            'You are a legend of Slavic legend and a skilled spearman. In your eyes, high dexterity and damage is worth the reduction of armor.')
        champion = Bogatyr()
        return champion
    elif sessence == 'Magus':
        print('You selcted Magus as your starting class.')
        time.sleep(2)
        print(
            'You are a knowledgeable lone sorcerer who utilizes talismans and charms to channel the mystic arts into powerful, magical attacks.')
        champion = Magus()
        return champion

    else:
        quit

        # Champion
    return sessence


def randomenemy():
    if Rando.rand(2) < 2:
        enem = Exile()
    if Rando.rand(2) == 1:
        enem = Mutant()
    else:
        enem = RampartGolem()
    # enem = Exile() if Rando.rand(2)<2 and enem==Mutant() elif Rando.rand(2)=1 else RampartGolem()
    return enem


def ranks():
    # Rank system (bronze, silver, gold)
    if champion.renown >= 10:
        print('You have recieved the Copper rank!')
        champion.maxhp += 100

    if champion.renown >= 15:
        print('You have recieved the Bronze rank!')
        champion.maxhp += 100

    if champion.renown >= 20:
        print('You have recieved the Silver rank!')
        champion.maxhp += 100

    if champion.renown >= 25:
        print('You have recieved the Gold rank!')
        champion.maxhp += 100

    if champion.renown >= 30:
        print('You have recieved the Platinum rank!')
        champion.maxhp += 100

    if champion.renown >= 10:
        print('Congratulations, you have recieved the Diamond rank!')
        champion.maxhp += 100


def charAttack():
    randomize = Rando.rand(20)
    if randomize >= champion.renown - enem.renown:
        print('You ready your', champion.weapon, '!')
        print('You attacked with your', champion.weapon, '!')
        if champion.starter == 'Templar':
            randomizeR = Rando.rand(250)

        if champion.starter == 'Bogatyr':
            randomizeR = Rando.rand(320)

        if champion.starter == 'Magus':
            randomizeR = Rando.rand(400)
        print('for', randomizeR, 'HP!')

        enem.hp -= randomizeR
        # enemy attacked -HP

        print("The", enem.name, "has", enem.hp, "HP left!")
    else:
        print('The', enem.name, 'dodged your attack!')


def enemAttack():
    randomize = Rando.rand(20)
    if randomize >= enem.renown - champion.renown:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('The enemy recoils.')
        if enem.name == 'Rampart Golem':
            randomizeD = Rando.rand(300)
        elif enem.name == 'Mutant':
            randomizeD = Rando.rand(200)
        elif enem.name == 'Exile':
            randomizeD = Rando.rand(350)
        print('The', enem.name, 'hit for', randomizeD, 'HP!')
        champion.hp -= randomizeD
        print('You now have', champion.hp, 'HP.')
    else:
        print('You dodged the enemys attack!')


def Attacks():
    if champion.starter == 'Templar':
        print(champion.weapon)
        # attack
        print('Campbell Soup')
        # healing item
        print('Bag')
        # inventory
        print('Run')
        # pass

        attackop = input('-=-=-=-= Select an Option =-=-=-=-')
        if attackop == (champion.weapon):
            charAttack()
        if attackop == 'Campbell Soup':
            print('You healed 250HP from the Campbell Soup!')
            champion.hp += 250
        if attackop == 'Bag':
            print(champion.bag)
        if attackop == 'Run':
            pass

    if champion.starter == 'Bogatyr':
        print(champion.weapon)
        print('Vodka Flask')
        # healing item
        print('Bag')
        print('Run')

        attackop = input('-=-=-=-= Select an Option =-=-=-=-')
        if attackop == (champion.weapon):
            charAttack()
        if attackop == 'Vodka Flask':
            print('You healed 255HP from the Vodka!')
            champion.hp += 255
        if attackop == 'Bag':
            print(champion.bag)
        if attackop == 'Run':
            pass

    if champion.starter == 'Magus':
        print(talisman)
        # magic attack
        print('Potions of Regeneration')
        # healing item
        print('Bag')
        print('Run')

        attackop = input('-=-=-=-= Select an Option =-=-=-=-')
        if attackop == (talisman):
            charAttack()
        if attackop == 'Potion of Regeneration':
            print('You healed 300HP from the Potion of Regeneration!')
            champion.hp += 300
        if attackop == 'Bag':
            print(champion.bag)
        if attackop == 'Run':
            pass


enem = randomenemy()
champion = essence()

while True:
    if enem.hp <= 0:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(enem.name, 'FALLEN.')
        champion.renown += enem.renown
        print('RENOWN EMBRACED.')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        enem = randomenemy()
    if champion.hp <= 0:
        print('YOU DIED')
        print('Final Renown Total:', champion.renown)

    Attacks()
    enemAttack()