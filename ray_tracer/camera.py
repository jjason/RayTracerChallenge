import math

from canvas import Canvas
from matrix import Matrix
from point import Point
from ray import Ray


class Camera:
    def __init__(self,
                 horizontal_size=100,
                 vertical_size=100,
                 field_of_view=math.pi,
                 transform=None):
        self._horizontal_size = horizontal_size
        self._vertical_size = vertical_size
        self._field_of_view = field_of_view
        self.transform = transform if transform else Matrix.identity(dimensions=4)

        # Sine we are likely to perform multiple calculations with this camera,
        # go ahead and cache the inverse of the transform as well as the
        # transformed origin.
        self._inverse_transform = self._transform.inverse()
        self._origin = self._inverse_transform * Point(x=0, y=0, z=0)

        half_view = math.tan(self._field_of_view / 2)
        aspect = self._horizontal_size / self._vertical_size

        if aspect >= 1:
            self._half_width = half_view
            self._half_height = half_view / aspect
        else:
            self._half_width = half_view * aspect
            self._half_height = half_view

        self._pixel_size = (self._half_width * 2) / self._horizontal_size

    @property
    def horizontal_size(self):
        return self._horizontal_size

    @property
    def vertical_size(self):
        return self._vertical_size

    @property
    def field_of_view(self):
        return self._field_of_view

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, value):
        self._transform = value

        # Sine we are likely to perform multiple calculations with this camera,
        # go ahead and cache the inverse of the transform as well as the
        # transformed origin.
        self._inverse_transform = self._transform.inverse()
        self._origin = self._inverse_transform * Point(x=0, y=0, z=0)

    @property
    def pixel_size(self):
        return self._pixel_size

    def ray_for_pixel(self, x=0, y=0):
        """
        Given the coordinates (x,y) of a pixel on a canvas, compute the ray that
        goes from the camera through the pixel on the canvas.

        :param x: Integer, the x coordinate of the pixel on the canvas
        :param y: Integer, the y coordinate of the pixel on the canvas
        :return: Ray, the ray that starts at the camera and goes through the
                      pixel on the canvas.  The direction component of the ray
                      will be normalized.
        """
        # Compute the offset, from the edge of the canvas, to the center of the
        # pixel
        x_offset = (x + 0.5) * self._pixel_size
        y_offset = (y + 0.5) * self._pixel_size

        # Compute the untransformed coordinates of the pixel in world space.
        # Since the camera looks toward -z in untransformed world, +x is to the
        # left.
        world_x = self._half_width - x_offset
        world_y = self._half_height - y_offset

        # Using the camera's matrix, transform the canvas point (remember that
        # canvas is at z=-1).  Then compute the ray's  direction (i.e., from
        # origin to pixel, and normalize it.
        pixel = self._inverse_transform * Point(x=world_x, y=world_y, z=-1)
        direction = (pixel - self._origin).normalize()

        return Ray(origin=self._origin, direction=direction)

    def render(self, world):
        """
        Given a world, render it using the camera's view of the world onto a
        canvas.

        :param world: World, the world to render
        :return: Canvas, a canvas representing the pixels for the image that
                         represents rendering the world from the camera's view.
        """
        image = Canvas(width=self._horizontal_size, height=self._vertical_size)
        # For every pixel in the canvas, compute the ray from the camera to the
        # pixel on the canvas and then figure out the color of the pixel as the
        # ray passes through the world
        for y in range(self._vertical_size):
            for x in range(self._horizontal_size):
                ray = self.ray_for_pixel(x=x, y=y)
                color = world.color_at(ray=ray)
                image.set_pixel(x=x, y=y, color=color)

        return image
