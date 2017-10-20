from ball import Ball

MAX_RADIUS = 40
NUM_BALLS = 20
balls = []


def setup():
    size(500, 720)
    fill(255)
    noStroke()

    for i in range(NUM_BALLS):
        balls.append(
            Ball(random(width), random(height), random(MAX_RADIUS / 2.0, MAX_RADIUS))
        )


def draw():
    background(0)

    for (i, ball) in enumerate(balls):
        ball.move()
        ball.collide(balls[i + 1:])
        ball.display()


# Create a new file called "ball.py" and type this code in.

SPRING = .05
GRAVITY = 0
FRICTION = 1


class Ball(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (random(255), random(255), random(255))

        self.vx = random(-1, 1) * 3
        self.vy = random(-1, 1) * 3

    def collide(self, others):
        for other in others:
            dx = other.x - self.x
            dy = other.y - self.y
            minDist = other.radius + self.radius
            if dist(other.x, other.y, self.x, self.y) < minDist:
                angle = atan2(dy, dx)

                targetX = self.x + cos(angle) * minDist
                targetY = self.y + sin(angle) * minDist

                ax = (targetX - other.x) * SPRING
                ay = (targetY - other.y) * SPRING
                self.vx -= ax
                self.vy -= ay
                other.vx += ax
                other.vy += ay

    def move(self):
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        if self.x + self.radius > width:
            self.x = width - self.radius
            self.vx *= -FRICTION
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx *= -FRICTION

        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy *= -FRICTION
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy *= -FRICTION

    def display(self):
        # I messed around with different fill methods here.  Change this function
        # to make the balls flash colors or just do different color things

        fill(
            self.color[0] * cos(self.x / width),
            self.color[1] * sin(self.y / height),
            self.color[2] * tan(self.x / width / self.y / height)
        )

        fill(
            self.color[2] * tan(self.x / width / self.y / height),
            self.color[0] * cos(self.x / width),
            self.color[1] * sin(self.y / height)
        )

        stroke(255, 50)

        fill(random(255), random(255), random(255))

        ellipse(self.x, self.y, self.radius * 2, self.radius * 2)
