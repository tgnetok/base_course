class Puppy :

    states = ['Болеет', 'Выздоравливает', 'Здоров']

    def __init__ (self, index, state = states[0]) :

        self.index = index
        self.state = state

    def get_treatment (self)