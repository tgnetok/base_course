class Puppy :

    states = ['Здоров', 'Выздоравливает', 'Болеет']

    def __init__ (self, index, state = states[0]) :

        self.index = index
        self.state = state

    def get_treatment (self):

        if self.state == states[2] :
            self.state == states[1]
        elif self.state == states[1] :
            self.state == states[0]

puppy_1 = Puppy (1)