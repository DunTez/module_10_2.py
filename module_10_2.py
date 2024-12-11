from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        warriors = 100
        days = 0
        while warriors > 0:
            days += 1
            if warriors > self.power:
                warriors -= self.power
            else:
                warriors = 0
            print(f"{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.")
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
print(f'Все битвы закончились!')
