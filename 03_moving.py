RADIUS = 40
x = RADIUS + 10
y = RADIUS + 10


def setup():
    size(1080, 720)
    fill(255)
    noStroke()


def draw():
    global x, y
    # mess around with background and +=1
    background(100)

    if mousePressed:
        fill(0)
    else:
        fill(255)

    x += 1
    y += 1

    ellipse(x, y, 2 * RADIUS, 2 * RADIUS)
