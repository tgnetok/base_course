class Planet :

    planet_count = 7

    def __init__ (self, mass_planet_1, mass_planet_2) :

        self.mass_planet_1 = mass_planet_1
        self.mass_planet_2 = mass_planet_2
    
    @property
    def planets_mass (self) :
        print (self.planet_1 + self.planet_2)

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
            
planet_1 = Planet (6 * 10 ** 24, 4 * 10 ** 25)
planet_1.planets_mass
Planet.name_planet ('Earth')
Planet.how_many_planets ()