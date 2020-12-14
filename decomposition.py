
class car:
    
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'parked'
        self._engine = Engine(cylinders=4)

    def speed_up(self, type='slow'):
        if type == 'fast':
            self._engine.gasoline_injection(10)
        else:
            self._engine.gasoline_injection(3)

        self._state = 'moving'


class Engine:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self.temperature = 0

    def gasoline_injection(self, amount):
        pass
