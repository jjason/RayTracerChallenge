#!/usr/bin/env python3

import math
from ray_tracer.canvas import Canvas
from ray_tracer.color import Color
from ray_tracer.matrix import Matrix
from ray_tracer.point import Point
from ray_tracer.ray import Ray
from ray_tracer.sphere import Sphere
from ray_tracer.vector import Vector

# Given a sphere, cast rays from the starting point (i.e., the ray's origin)
# to each point on the wall behind the sphere and for every ray that intersects
# the sphere cast a "shadow" on the wall by painting a red pixel.

# We are going to start the ray at z = -5
ray_origin = Point(x=0, y=0, z=-5)

# The "wall" that the shadow will be cast upon is at z = 10
wall_z = 10

# The "wall" needs to be at least big enough to hold entire shadow.  With the
# unit sphere at the origin, if the light source is at z = -5 and the wall is at
# z = 10, the wall needs to be at least 6 units across.
wall_size = 7.0
half_wall_size = wall_size / 2

# The canvas will be 100 pixels on a side
canvas_pixels = 100

# The size of a pixel in world space units
pixel_size = wall_size / canvas_pixels

# We are going to take the easy approach for now.  If we were so inclined, since
# we know that the sphere is centered on the canvas, we could start at the
# center pixel and move out to one side until it no longer intersects.  For each
# intersection we draw a red pixel and can also draw three more pixels in the
# equivalent position in the other quadrants.

canvas = Canvas(width=canvas_pixels, height=canvas_pixels)
red = Color(red=1, green=0, blue=0)
sphere = Sphere()

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
        # be the direction of our light ray.
        wall_position = Point(x=world_x, y=world_y, z=wall_z)
        direction = wall_position - ray_origin

        # NOTE - may need to go back and fix this.  At the time, because only
        # vectors had magnitude and could be normalized those methods were
        # defined on the Vector class and not Tuple.  That _may_ still be the
        # right thing to do.  It may be that what should happen in the tuple
        # class is when an arithmetic operation is performed on a tuple, the
        # correct subclass is instantiated.  For now, we are going to manually
        # create a Vector from the tuple.
        direction = Vector.normalize(Vector(x=direction.x,
                                            y=direction.y,
                                            z=direction.z))

        ray = Ray(origin=ray_origin, direction=direction)

        # If the ray intersects the sphere, then the x, y coordinate is to be
        # colored red
        if sphere.intersect(ray=ray).hit() is not None:
            canvas.set_pixel(x=x, y=y, color=red)

with open("cast_rays_at_sphere.ppm", "w") as file:
    file.write(canvas.to_ppm())
