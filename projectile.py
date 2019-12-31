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
                        velocity=Vector.normalize(Vector(x=1, y=1, z=0)))
environment = Environment(gravity=Vector(x=0, y=-0.1, z=0),
                          wind=Vector(x=-0.01, y=0, z=0))

while projectile.position.y >= 0:
    print("Projectile position: {}".format(projectile.position))
    projectile.tick(environment)
