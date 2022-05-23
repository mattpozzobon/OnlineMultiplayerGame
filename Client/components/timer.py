
class Timer:
    def __init__(self, info):
        self.info = info
        self.time = 0

    def render(self):
        temp = self.info[0].clock.get_time()
        if self.time >= 0:
            self.time -= temp

    def add(self, x):
        self.time = x*1000

    def get(self):
        if self.time > 0:
            return round(self.time/1000)
        else:
            return 0