




class MoneyBox:
    def __init__(self, capacity):
        self.total = 0
        self.capacity = capacity
        pass
# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.total + v <= self.capacity:
            print(f'Было {self.total} монет')
            return True
        else:
            return False
# True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v) == True:
            self.total += v
            print(f'В копилке {self.total} монет')
            return True
        else:
            print(f'В копилку не помещается {v} монет')
            return False
# положить v монет в копилку

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)













