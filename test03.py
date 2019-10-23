import threading
import time


class Taread01(threading.Thread):
    def __init__(self, target=None, args=()):
        super(Taread01, self).__init__()
        self.target = target
        self.args = args
        self.result = None

    def run(self):
        self.result = self.target(*self.args)

    def get_data(self):
        threading.Thread.join(self)
        return self.result


def fun(a, b):
    time.sleep(2)
    return a + b


p1 = Taread01(target=fun, args=(2, 3))
p2 = Taread01(target=fun, args=(3, 4))
p1.start()

p2.start()

print(p1.get_data())
print(p2.get_data())
