class Businessman :

    def_name = 'Baigashov'
    def_age = 30

    def __init__ (self, name = def_name, age = def_age) :

        self.name = name
        self.age = age
        self._money = 20000
        self._business = 'astronomy'

    def info (self) :
        
        print (self.name)
        print (self.age)
        print (self._business)
        print (self._money)

    def def_info (self) :

        print (self.def_name)
        print (self.def_age)

    def _make_deal (self, _business_name, _business_cost) :
        
        self._business += f', {_business_name}'
        self._money -= _business_cost

    def earn_money (self, _money) :

        self._money += _money

    def buy_business (self) :



businessman_1 = Businessman ()
businessman_1.earn_money (2000)
businessman_1._make_deal ('spaceship', 300)
businessman_1.info ()