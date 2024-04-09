from random import randint
import json

class events():
    def __init__(self):
        f = open('evets.txt', 'r', encoding = 'utf-8')
        self.events = json.loads(f.read())


    def event_create(self):
        return self.events[randint(0,2)]



class character():
    def __init__(self):
        self.name = input('введите имя\n')
        self.health = 100
        self.armor = int(input('класс брони?\n'
                               '3\n'
                               '4\n'
                               '5\n'))
        self.stamina = 100//self.armor-1
        self.luck = randint(0, 100)
        self.food = 100


class game():
    def __init__(self):
        self.game_engine = events()
        self.pmc = character()


    def add_parameters(self, list):

        param = ''.join(list).split('?')
        match str(param[0]):
            case 'luck':
                self.pmc.luck += int(param[1])
            case 'health':
                self.pmc.health += int(param[1])
            case 'food':
                self.pmc.food += int(param[1])
            case 'stamina':
                self.pmc.stamina += int(param[1])

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
    def start(self):
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



misha = game()
misha.start()