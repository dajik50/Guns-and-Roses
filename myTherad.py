from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs=None):
        super().__init__()
        self.func = target
        self.a = args
        self.b = kwargs

    def run(self) -> None:
        try:
            self.func(*self.a, **self.b)
        except Exception:
            return None


def player(sec, song):
    for i in range(3):
        print("Playing %s: %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'})
t.start()
t.join()
