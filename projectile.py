#!/usr/bin/env python3

from ray_tracer.canvas import Canvas
from ray_tracer.color import Color
from ray_tracer.point import Point
from ray_tracer.vector import Vector

class Environment:
    def __init__(self, gravity=Vector(), wind=Vector()):
        self.gravity = gravity
        self.wind = wind


class Projectile:
    def __init__(self, position=Point(), velocity=Vector()):
        self.position = position
        self.velocity = velocity

    def tick(self, environment=Environment()):
        self.position += self.velocity
        self.velocity = self.velocity + environment.gravity + environment.wind


projectile = Projectile(position=Point(x=0, y=1, z=0),
                        velocity=Vector(x=1, y=1.8, z=0).normalize() * 11.25)
environment = Environment(gravity=Vector(x=0, y=-0.1, z=0),
                          wind=Vector(x=-0.01, y=0, z=0))

canvas = Canvas(width=900, height=550)
red = Color(red=1, green=0, blue=0)

while projectile.position.y >= 0:
    print("Projectile position: {}".format(projectile.position))
    x = min(899, max(0, int(projectile.position.x)))
    y = min(549, max(0, int(549 - projectile.position.y)))
    canvas.set_pixel(x=x, y=y, color=red)
    projectile.tick(environment)

with open("projectile.ppm", "w") as file:
    file.write(canvas.to_ppm())
