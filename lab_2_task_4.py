class Planet :

    planet_count = 7

    def __init__ (self) :
        pluto = int(input('Плутон - планета? '))
        if pluto == 'Да' :
            Planet.planet_count = Planet.planet_count + 1
        elif pluto == 'Нет' :
            Planet.planet_count = 7
        else :
            print ('Да или нет?')

    @classmethod
    def how_many_planets (cls) :
        pluto = int(input('Плутон - планета? '))
        if pluto == 'Да' :
            planet_count = planet_count + 1
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

Planet.name_planet ('Earth')
Planet.classmethod ()

