class Ball:

    color = 'red'
    radius = 5

ball = Ball ()

print (ball.color)
print (Ball.radius)

ball.color = 'white'
print (ball.color)
print (Ball.color)

Ball.color = 'white'
new_ball = Ball ()
print (Ball.color)
print (new_ball.color)