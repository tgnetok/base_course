class Ball:

    def __init__(self, mass):

        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0

    # Методы, реализующие поведение экземпляров
    # self – подразумеваемый экземпляр
    def drop (self):
        print('Я подбросился')
        self.y = 2

    def kick (self):
        print ('Я пнулся')
        self.x += 1

    def fail (self) :
        self.mass = self.mass - 0.1

ball = Ball(0.5)

ball.drop ()
ball.kick ()
ball.fail ()
print (ball.x)
print (ball.y)
print (ball.mass)

ball_2 = Ball (1)
ball_2.kick ()
ball_2.kick ()
ball_2.kick ()
print (ball_2.x)
print (ball.x)