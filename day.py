from random import randint

class State:
    def __init__(self):
        self.time = 0
        self.mood = 50
        self.energy = 0
        self.hunger = 20
        self.state = 'I am sleeping.'
        self.money = 100
        self.calls = 0
        self.meals = 0
        self.weather = 5

    def sleep(self):
        self.state = 'I am sleeping.'
        self.energy = min(self.energy + 20, 100)
        self.hunger = max(self.hunger - 5, 0)

    def eat(self):
        self.state = 'I am eating.'
        self.hunger = 0
        self.energy = min(self.energy + 20, 100)
        self.money = self.money - randint(20,40)
        if self.money < 0:
            self.money = 0
            self.hunger = 30
        self.meals = self.meals + 1

    def study(self):
        self.state = 'I am studying.'
        self.energy = max(self.energy - 10, 0)
        self.mood = max(self.mood - 10, 0)

    def comunicate(self, people):
        self.state = 'I am talking with friends.'
        self.mood = min(self.mood + 10 * people, 100)
        self.energy = min(self.energy + 20, 100)

    def call(self):
        self.state = 'I am calling my parents.'
        self.mood = min(self.mood + 10, 100)
        self.calls = 1

    def go_walking(self):
        self.state = 'I am going for a walk.'
        self.mood = min(self.mood + 10, 100)
        self.energy = max(self.energy - 10, 0)
        self.hunger = min(self.hunger + 10, 0)
    
    def day(self):
        while self.time <= 24:
            print('It`s', self.time, ': 00 on the clock.')
            self.weather = randint(1, 10)
            if self.energy == 0 or (self.energy <= 60 and (self.time >= 22 or self.time <=8)):
                self.sleep()
            elif self.hunger >= 50 and self.meals <= 2:
                self.eat()
            elif self.energy >= 30 and self.mood >=10:
                self.study()
            elif randint(1,10) >= 8 and self.calls == 0:
                self.call()
            elif self.mood <= 50 and self.weather >=8:
                self.go_walking()
                if self.money >= 30:
                    self.state = self.state + ' I am buying an ice cream.'
                    self.hunger = max(self.hunger - 10, 0)
                    self.mood = min(self.mood + 10, 100)
                    self.money = self.money - 20
            else:
                self.comunicate(randint(1, 3))
            
            if randint(1, 100) == 69:
                self.time = int((self.time - 5) % 24)
                print('Wow! I am suddenly timetravelling!')
            
            print(self.state)

            self.energy = max(self.energy - 10, 0)
            self.hunger = min(self.hunger + 10, 100)
            self.time = self.time + 1

State().day()