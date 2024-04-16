import os
from random import randint
import json
import ascii

class events():
    def __init__(self):
        f = open('evets.txt', 'r', encoding = 'utf-8')
        self.events = json.loads(f.read())


    def event_create(self):
        return self.events[randint(0,2)]



class character():
    def __init__(self):
        self.name = input('введите имя\n')
        self.gun = int(input('какое оружие?\n1)TT\n2)AK47\n'))
        self.health = 100
        self.armor = int(input('класс брони?\n'
                               '3\n'
                               '4\n'
                               '5\n'))
        self.stamina = (100//self.armor-1)//self.gun
        self.luck = randint(0, 100)
        self.food = 100
        self.player = 'pmc'
        self.state = None
class g_enemy():
    def __init__(self, gun, armor, player):
        self.name = ascii.name()
        self.gun = gun
        self.armor = armor
        self.health = 100
        self.food = randint(35,99)
        self.player = player
        self.stamina = (100 // int(self.armor) - 1) // int(self.gun)
        self.state = None

class game():
    def __init__(self):
        self.game_engine = events()
        self.pmc = character()

    def fight_check_health(self, body):
        if int(body.health) > 100:
            body.health = 100


    def add_parameters(self, list):

        param = ''.join(list).split('?')
        match str(param[0]):
            case 'luck':
                self.pmc.luck += int(param[1])
                if self.pmc.luck > 100:
                    self.pmc.luck = 100
                else: print(f'{param[1]} удачи')
            case 'health':
                self.pmc.health += int(param[1])
                if self.pmc.health > 100:
                    self.pmc.health = 100
                else: print(f'{param[1]} здоровья')
            case 'food':
                self.pmc.food += int(param[1])
                if self.pmc.food > 100:
                    self.pmc.food = 100
                else: print(f'{param[1]} еды')
            case 'stamina':
                self.pmc.stamina += int(param[1])
                if self.pmc.stamina > 100:
                    self.pmc.stamina = 100
                else: print(f'{param[1]} выносливости')
            case 'fight':
                self.fight(param[1], param[2], param[3])

        pass



    def event_req(self, event_, choice_):
        req = ''.join(list(list(event_.items())[0][1][choice_-1].items())[0][1][0]).split('?')
        answer = 1
        match str(req[0]):
            case 'luck':
                if self.pmc.luck >= int(req[1]): answer = 2
            case 'health':
                if self.pmc.health >= int(req[1]): answer = 2
            case 'armor':
                if self.pmc.armor >= int(req[1]): answer = 2
            case 'stamina':
                if self.pmc.stamina >= int(req[1]): answer = 2
            case 'food':
                if self.pmc.food >= int(req[1]): answer = 2


        return answer




    def pmc_params(self, body):
        return (f"""{body.name}:\n
Здоровье:\n[{'*' * (body.health // 4) + ('-' * (25 - body.health // 4))}]
Выносливость:\n[{'*' * (body.stamina // 4) + ('-' * (25 - body.stamina // 4))}]
Еда:\n[{'*' * (body.food // 4) + ('-' * (25 - body.food // 4))}]
Класс брони: {body.armor}
Тип игрока: {body.player}
Оружие: {'AK47' if int(body.gun) == 2 else 'TT'}\n""")

    def fight(self, gun = str, armor = int, player = str):
        enemy = g_enemy(gun, armor, player)

        os.system('cls')
        print('завязался движ')
        while int(self.pmc.health) > 0 and int(enemy.health > 0):
            if self.pmc.health <= 0:
                print('вы умерли')
                exit()

            os.system('cls')

            enemy.state = ascii.rand_state()

            print('\n', self.pmc_params(enemy), '\n', self.pmc_params(self.pmc))
            print('\n', enemy.name, enemy.state, )

            state_pmc = input('ваше действие?\n'
                                   '1)открыть огонь\n'
                                   '2)начать лечиться\n'
                                   '3)спрятаться за стену\n')
            pmc_states = {'1': 'открыть огонь', '2': 'начать лечиться','3': 'спрятаться за стену'}
            self.pmc.state = pmc_states[state_pmc]

            if enemy.state == 'спрятался за стену' and self.pmc.state == 'открыть огонь':
                print('\n вы стреляете в стену...\n')
            elif enemy.state == 'спрятался за стену' and self.pmc.state == 'начать лечиться':
                print('\n лечимся\n')
                self.pmc.health += 20
            elif enemy.state == 'спрятался за стену' and self.pmc.state == 'спрятаться за стену':
                print('\n ура, игра в прятки\n')
            elif enemy.state == 'открыл огонь' and self.pmc.state == 'открыть огонь':
                print('\n ну нормально пострелялись\n')
                self.pmc.health -= (70*int(enemy.gun)) // int(self.pmc.armor)
                enemy.health -= (70*int(self.pmc.gun)) // int(enemy.armor)
            elif enemy.state == 'открыл огонь' and self.pmc.state == 'начать лечиться':
                print('\n вы получили маслину\n')
                self.pmc.health -= (70 * int(enemy.gun)) // int(self.pmc.armor)
            elif enemy.state == 'открыл огонь' and self.pmc.state == 'спрятаться за стену':
                print('\n везет что он такой глупый\n')

            elif enemy.state == 'начал лечиться' and self.pmc.state == 'открыть огонь':
                print('\n вы попали 0_o\n')
                enemy.health -= (70 * int(self.pmc.gun)) // int(enemy.armor)
            elif enemy.state == 'начал лечиться' and self.pmc.state == 'начать лечиться':
                print('\n перемирие?...\n')
                self.pmc.health += 20
                enemy.health += 20
            elif enemy.state == 'начал лечиться' and self.pmc.state == 'спрятаться за стену':
                print('\n ну давай посмотрим как он лечится, да-да\n')
                enemy.health += 20

            self.fight_check_health(enemy)
            self.fight_check_health(self.pmc)
            cl = input('для продолжения нажмите любую клавищу\n')
        print('у вас получилось!!!')
        ascii.rand_bonus(self.pmc)

        pass




    def start(self):
        print(self.pmc_params(self.pmc))
        os.system('cls')
        print("вы участник организации 'USEC', ваша цель выйти из рейда живым. Удачи!")

        for i in range(20):

            if self.pmc.health <= 0:
                print("вы умерли, игра окончена")
                break
            event = self.game_engine.event_create()
            choice = int(input(f"{list(event.keys())[0]}, \n"
                  f"1){list(list(event.items())[0][1][0])[0] }\n"
                  f"2){list(list(event.items())[0][1][1])[0] }\n"
                  f"3){list(list(event.items())[0][1][2])[0] }\n"
                  f"4){list(list(event.items())[0][1][3])[0] }\n"))
            print(f"{list(list(event.items())[0][1][choice-1].items())[0][1][self.event_req(event, choice)][0] }\n")
            self.add_parameters(list(list(event.items())[0][1][choice-1].items())[0][1][self.event_req(event, choice)][1])
            cl = input('для продолжения нажмите любую клавищу\n')
            os.system('cls')





misha = game()
misha.start()