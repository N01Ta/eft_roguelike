import random
def name():
    names = ['Акакий', 'Смауг', 'Монки', 'Гималай', 'Демократ', 'Трактор', 'Миша', 'Ярослэйв', 'Матвей', 'Санек', 'Сан Саныч', 'Трафаретыч', 'Михаил Стреляный', 'Отвертыч Картовый', 'Вячеслав Жижин']
    return random.choice(names)
def rand_state():
    states = ['спрятался за стену', 'открыл огонь', 'начал лечиться']
    return random.choice(states)

def rand_bonus(body):
    bonuses = ['health', 'food', 'stamina', 'luck']
    capital = random.randint(10, 40)
    body.food += capital
    print('+', capital, 'еды')


class arts:
    pass