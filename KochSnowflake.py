import turtle

"""
Draw Koch Snowflake
"""
SCREENSIZE = 1000

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)

# Initialize
t = turtle.Turtle()

# Set Params
t.penup()
t.setpos(-1 * SCREENSIZE / 2, 0)
t.pendown()
t.speed(0)

# Draw Koch Snowflake
koch(t, 4, SCREENSIZE)

turtle.done()