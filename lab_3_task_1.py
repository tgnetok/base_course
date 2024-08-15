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

    @classmethod
    def def_info (self) :

        print (self.def_name)
        print (self.def_age)

    def _make_deal (self, _business_name, _business_cost) :
        
        self._business_name = _business_name
        self._business_cost = _business_cost

    def earn_money (self, _money) :

        self._money += _money

    def buy_business (self, _business_name, _discount) :

        if self._money > self._business_cost * (1 - _discount) :
             
            self._business += f', {_business_name}'
            self._money -= self._business_cost * (1 - _discount)

        else :

            print ('Недостаточно денег на счету.')


class Business :

    def __init__ (self, _area, _price) :

        self._area = _area
        self._price = _price

    def final_price(self, _price_discount) :

        self._price *= (1 - _price_discount)


class RestarauntBusiness (Business) :

    def __init__(self, _profit = 50000000) :

        self._profit = _profit



if __name__ == '__main__' :

    Businessman.def_info ()
    businessman_1 = Businessman ()
    businessman_1.info ()
    restaraunht_1 = RestarauntBusiness
    businessman_1._make_deal ('spaceship', 88005553535)
    businessman_1.buy_business ('spaceship', 0.2)
    businessman_1.earn_money (400000000000)
    businessman_1.buy_business ('spaceship', 0.2)
    businessman_1.info ()