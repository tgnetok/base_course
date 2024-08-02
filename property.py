class SummatorClass :
    def __init__ (self, a, b) :
        self.a = a
        self.b = b

    @property
    def sum_two_num (self) :
        hehehehe = (f'Сумма двух чисел равна {self.a + self.b}')
        print (hehehehe)

sum_cls = SummatorClass (1, 2)
sum_cls.sum_two_num