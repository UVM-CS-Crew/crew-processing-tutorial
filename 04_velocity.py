RADIUS = 40
x = RADIUS + 10
y = RADIUS + 10
vx = 1
vy = 1


def setup():
    size(500, 720)
    fill(255)
    noStroke()


def draw():
    global x, y, vx, vy
    # mess around with background and (x,y,vx,vy)+=1
    background(100)

    if mousePressed:
        fill(0)
    else:
        fill(255)

    x += vx
    y += vy

    if x - RADIUS <= 0 or x + RADIUS >= width:
        vx *= -1
    if y - RADIUS <= 0 or y + RADIUS >= height:
        vy *= -1

    ellipse(x, y, 2 * RADIUS, 2 * RADIUS)
    fill(120)
    ellipse(x, y, 10, 10)
