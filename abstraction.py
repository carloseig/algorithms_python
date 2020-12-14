
class Washing_machine:
    
    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_container(temperature)
        self._add_detergent()
        self._wash()
        self._spin_dry()

    def _fill_container(self, temperature):
        print(f'Filling the container with {temperature} water')

    def _add_detergent(self):
        print('Adding detergent')

    def _wash(self):
        print('Washing the clothes')

    def _spin_dry(self):
        print('Spin drying the clothes')


if __name__ == '__main__':
    washing_machine = Washing_machine()
    washing_machine.wash()
