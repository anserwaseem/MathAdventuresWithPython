# Creating balls of different sizes (5 to 50 units randomly) using CLASS and METHODS.

ballList = []  # empty list to put the balls in

class Ball:
    def __init__(self, x, y):
        '''initializing a Ball'''
        self.xcor = x
        self.ycor = y
        self.xvel = random(-2, 2)
        self.yvel = random(-2, 2)
        self.col = color(random(255), random(255), random(255))
        self.sz = random(5, 50)

    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        # if the ball reaches a wall, switch direction
        if self.xcor > width or self.xcor < 0:
            self.xvel = -self.xvel
        if self.ycor > height or self.ycor < 0:
            self.yvel = -self.yvel
        fill(self.col)
        ellipse(self.xcor, self.ycor, self.sz, self.sz)

def setup():
    size(600, 600)
    for i in range(100):
        ballList.append(Ball(random(width), random(height)))

def draw():
    background(0)  # black
    for ball in ballList:
        ball.update()
