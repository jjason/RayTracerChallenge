import math

from ray_tracer.canvas import Canvas
from ray_tracer.color import Color
from ray_tracer.matrix import Matrix
from ray_tracer.point import Point

canvas = Canvas(width=400, height=400)
red = Color(red=1, green=0, blue=0)

# Assume that the clock is oriented such that the face is perpendicular to the
# z axis.  12 o'clock is at the point (0, 1, 0), 3 o'clock at (1, 0, 0), 6
# o'clock at (0, -1, 0), and 9 o'clock at (-1, 0, 0).  We are going to rotate
# the 12 o'clock point around the z axis (remember that since we are in a left-
# handed system we need to do a negative rotation to go "clockwise") then scale
# it by the portion of the canvas the clock face will occupy and then translate
# it so that the point (0, 0, 0) is at the center of the canvas.  We then plot
# the x/y coordinates of the point onto the canvas, remembering that the y
# coordinate on the canvas increases as it goes down while in our 3-d space y
# increases as it goes up
for time in range(12):
    transform = Matrix.identity().rotate_z(radians=-time * math.pi/6).scale(x=150, y=150).translate(x=200, y=200)
    point = transform * Point(0, 1, 0)
    print("{} = {}".format(time, point))
    canvas.set_pixel(x=int(point.x), y=400 - int(point.y), color=red)

with open("clock.ppm", "w") as file:
    file.write(canvas.to_ppm())
