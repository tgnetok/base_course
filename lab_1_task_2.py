class Pyramid :

    def __init__ (self, max_h, bricks_count = 0) :

        self.max_h = max_h
        self.bricks_count = bricks_count
    
    def add_bricks (self, bricks) :
        self.bricks_count = self.bricks_count + bricks 

    def get_height (self) :
        print (self.bricks_count)
 
    def is_done (self, brks = 0) :

        for i in range (0, self.max_h, 1) :
            brks += 1
        if self.bricks_count == 0 :
            print ('Сначала задайте количество кирпичей.')
        else :
            procent = (brks / self.bricks_count) * 100
            print (f'{procent} % сделано.')
            print (brks)


pyramid_1 = Pyramid (8)
pyramid_1.add_bricks (6)
pyramid_1.is_done ()