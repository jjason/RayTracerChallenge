#!/usr/bin/env python3

import math

from ray_tracer.camera import Camera
from ray_tracer.color import Color
from ray_tracer.lights import PointLight
from ray_tracer.materials import Material
from ray_tracer.matrix import Matrix
from ray_tracer.plane import Plane
from ray_tracer.point import Point
from ray_tracer.sphere import Sphere
from ray_tracer.vector import Vector
from ray_tracer.world import World

# Given a world represented by 6 spheres, three of the flattened to look like
# two walls and a floor, render them using a camera and world

# The floor:
floor = Plane(material=Material(color=Color(red=1, green=0.9, blue=0.9),
                                specular=1))

# The right wall
right_wall = Plane(material=floor.material)
right_wall.transform = Matrix.translation_transform(x=0, y=0, z=5) * \
                       Matrix.rotation_x_transform(radians=math.pi/2)


# For the large sphere in the middle, create a unit sphere that is translated
# upward slightly and is colored green
middle_sphere = Sphere(transform=Matrix.translation_transform(x=-0.5,
                                                              y=1,
                                                              z=0.5),
                       material=Material(color=Color(red=0.1,
                                                     green=1,
                                                     blue=0.5),
                                         diffuse=0.7,
                                         specular=0.3))

# For the smaller sphere on the right, scale it to half size and color red
right_sphere = Sphere(transform=Matrix.translation_transform(x=1.5,
                                                             y=0.5,
                                                             z=-0.5) *
                                Matrix.scaling_transform(x=0.5, y=0.5, z=0.5),
                      material=Material(color=Color(red=1, green=0.1, blue=0.1),
                                        diffuse=0.7,
                                        specular=0.3))

# For the smallest sphere, scale it by 1/3 and translate, color blue
left_sphere = Sphere(transform=Matrix.translation_transform(x=-1.5,
                                                            y=0.33,
                                                            z=-0.75) *
                               Matrix.scaling_transform(x=0.33, y=0.33, z=0.33),
                     material=Material(color=Color(red=0.1, green=0.1, blue=1),
                                       diffuse=0.7,
                                       specular=0.3))

# The world's light source is white and shining from above and to the left
world = World(objects=[floor,
                       right_wall,
                       middle_sphere,
                       right_sphere,
                       left_sphere],
              light_source=PointLight(position=Point(x=-10, y=10, z=-10),
                                      intensity=Color(red=1, green=1, blue=1)))

# Configure the camera
camera = Camera(horizontal_size=200,
                vertical_size=100,
                field_of_view=math.pi/3,
                transform=Matrix.view_transform(eye=Point(x=0, y=1.5, z=-5),
                                                to=Point(x=0, y=1, z=0),
                                                up=Vector(x=0, y=1, z=0)))

# Render the world
canvas = camera.render(world=world)

with open("chapter_9.ppm", "w") as file:
    file.write(canvas.to_ppm())
