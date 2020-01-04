#!/usr/bin/env python3

from ray_tracer.canvas import Canvas
from ray_tracer.color import Color
from ray_tracer.lights import PointLight
from ray_tracer.materials import Material
from ray_tracer.point import Point
from ray_tracer.ray import Ray
from ray_tracer.sphere import Sphere

# Given a sphere and a light source, figure out the color at every point that
# a ray cast from the eye to each point on the canvas intersects the sphere and
# set that corresponding pixel in the canvas to the color.

# We are going to start the ray at z = -5
ray_origin = Point(x=0, y=0, z=-5)

# We will position the wall at z=10
wall_z = 10

# The "wall" needs to be at least big enough to "hold" the entire rendered
# sphere so we have some black background.  With the unit sphere at the origin,
# if the light source is at z = -5 and the wall is at z = 10, the wall needs to
# be at least 6 units across.
wall_size = 7.0
half_wall_size = wall_size / 2

# The canvas will be 100 pixels on a side...making it too large takes a really
# long time to render
canvas_pixels = 100

# The size of a pixel in world space units
pixel_size = wall_size / canvas_pixels


canvas = Canvas(width=canvas_pixels, height=canvas_pixels)
material = Material(color=Color(red=1, green=0.2, blue=1))
sphere = Sphere(material=material)

# Create the light source for the image
light = PointLight(position=Point(x=-10, y=10, z=-10),
                   intensity=Color(red=1, green=1, blue=1))

# For every row of pixels in the canvas
for y in range(canvas_pixels):
    # Convert the y coordinate to its corresponding world coordinate
    world_y = half_wall_size - pixel_size * y

    # For every pixel in this row
    for x in range(canvas_pixels):
        # Convert the x coordinate to its corresponding world coordinate
        world_x = -half_wall_size + pixel_size * x

        # Now that we know the world x, y, and z (z is the wall position) we
        # can create the point on the wall in world space.  Since we know where
        # the light source origin is, we can create a vector as the difference
        # of those two points and then normalize it to a unit vector.  This will
        # be the direction of the ray from the eye to the wall.
        wall_position = Point(x=world_x, y=world_y, z=wall_z)
        direction = wall_position - ray_origin

        ray = Ray(origin=ray_origin, direction=direction.normalize())

        # If the ray intersects the sphere, then we need to figure out what the
        # color of the sphere is at that point and set the pixel accordingly.
        hit = sphere.intersect(ray=ray).hit()
        if hit is not None:
            # Figure out the position on the ray from the eye to where the ray
            # hit the sphere and then compute normal at that location
            position = ray.position(time=hit.time)
            normal = hit.the_object.normal_at(position=position)

            # The vector to the eye is the opposite of the ray direction
            eye = -ray.direction

            # Now we need to compute the color value for the position on the
            # sphere
            color = hit.the_object.material.lighting(light=light,
                                                 position=position,
                                                 eye=eye,
                                                 normal=normal)

            # Now set the corresponding pixel on the canvas to the color
            canvas.set_pixel(x=x, y=y, color=color)

with open("chapter_6.ppm", "w") as file:
    file.write(canvas.to_ppm())
