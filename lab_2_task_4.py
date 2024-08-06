class Planet :

    planet_count = 7


    def __init__ (self, ) :

        


    @classmethod
    def how_many_planets (cls) :
        pluto = input('Плутон - планета? ')
        if pluto == 'Да' :
            planet_count = 8
            print (planet_count)
        elif pluto == 'Нет' :
            planet_count = 7
        else :
            print ('Да или нет?')

    @staticmethod
    def name_planet(name):
        if name == 'Earth':
            print ('Home')
        else :
            print ('Not home')

    @property


Planet.name_planet ('Earth')
Planet.how_many_planets ()