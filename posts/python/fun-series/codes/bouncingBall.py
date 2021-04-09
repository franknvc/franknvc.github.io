import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color(random.choice(colors))
        self.shape(random.choice(shapes))

        self.penup()
        self.speed(0)
        self.goto(random.randint(-290, 290), random.randint(200, 450))
        self.dy = 0
        self.dx = random.randint(-3, 3)
        self.da = random.randint(-5, 5)

    def ball_animation(self):
        self.rt(self.da)
        self.dy -= gravity
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)

    def check_wall_collision(self):
        # Check for bounce off wall
        if self.xcor() >= 300 or self.xcor() <= -300:
            self.dx *= -1
            self.da *= -1

        # Check for bounce off ground
        if self.ycor() <= -300:
            self.sety(-300)
            self.dy *= -1
            self.da *= -1


window = turtle.Screen()
window.bgcolor("black")
window.title("Bouncing Ball Simulator")
window.tracer(10)

balls = []
colors = ["red", "blue", "yellow", "orange", "green", "magenta", "white"]
shapes = ["square", "circle", "triangle"]

for _ in range(15):
    balls.append(Ball())

gravity = 0.3

while True:
    window.update()

    for ball in balls:
        ball.ball_animation()
        ball.check_wall_collision()

    # check for collisions between the balls
    for i in range(0, len(balls)):
        for j in range(i + 1, (len(balls))):
            if balls[i].distance(balls[j]) < 20:
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
