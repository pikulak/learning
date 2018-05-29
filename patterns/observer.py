
class Observable:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.handle(self, *args, **kwargs)


class Car(Observable):

    def __init__(self):
        super().__init__()
        self.brand = self._get_brand()
        self._color = 'Default color'

    def _get_brand(self):
        assert hasattr(self, 'brand'), (
            f'Class {self.__class__.__name__} missing "brand" attribute'
        )
        return getattr(self, 'brand')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.notify(event='color_change')


class Mercedes(Car):
    brand = 'Mercedes'


class CarColorChangeHandler:

    @staticmethod
    def handle(subject, event):
        if event != 'color_change':
            return
        print(f'{subject.brand}\'s new color is: {subject.color}')


mercedes = Mercedes()
mercedes.attach(CarColorChangeHandler())
mercedes.color = 'white'    # stdout > Mercedes's new color is: white
